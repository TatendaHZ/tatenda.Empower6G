import asyncio
import websockets
import json
import requests
import time
from datetime import datetime
import prometheus_client as prom
import logging
import psutil
import socket
import signal
import sys
from functools import partial
import csv
import os
from bs4 import BeautifulSoup  # For latency/jitter scraping

# ---------------- Configuration ----------------
LOCAL = True
INTERVAL = 5  # Data collection interval in seconds
PROMETHEUS_NODE_IP = "192.168.88.40"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
PROMETHEUS_SERVER = 80  # Prometheus port
ALL_CSV_FILE = "four_days_metrics.csv"
MAX_UES = 3  # Maximum number of UEs to support in CSV columns
LATENCY_DASHBOARD_URL = "http://192.168.88.46/"  # Update as needed

if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"  # Amarisoft gNB
else:
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))

NODES = [
    {"name": "core_node", "ip": "192.168.88.38:9100"},
    {"name": "mec_node", "ip": "192.168.88.27:9100"},
    {"name": "kube_app_server", "ip": "192.168.88.40:9100"}
]

API_MESSAGE_ENB_UEGET = '{"message":"ue_get","stats": true}'

# ---------------- Prometheus Metrics ----------------
AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'Channel quality indicator (CQI)', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate in Mbps', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'Energy per resource element (EPRE) in dBm', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'Physical uplink shared channel (PUSCH) SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate in Mbps', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL path Loss (PUSCH) SNR in dB', ["ue"])

LATENCY_GAUGE = prom.Gauge('node_latency', 'Node latency in ms', ['node'])
JITTER_GAUGE = prom.Gauge('node_jitter', 'Node jitter in ms', ['node'])

prom_server = None

# ---------------- CSV Columns ----------------
CSV_COLUMNS = ['timestamp']
for node in NODES:
    node_name = node['name']
    for metric in ['cpu', 'memory', 'tx', 'rx', 'latency', 'jitter', 'cost']:
        CSV_COLUMNS.append(f'{node_name}_{metric}')
for ue_num in range(1, MAX_UES + 1):
    for metric in ['cqi', 'dl_bitrate', 'dl_mcs', 'epre', 'pusch_snr', 'ul_bitrate', 'ul_mcs', 'ul_path_loss']:
        CSV_COLUMNS.append(f'ue{ue_num}_{metric}')

# ---------------- Helper Functions ----------------
def kill_process_using_port(port):
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid:
                    process = psutil.Process(pid)
                    print(f"Found process {pid} ({process.name()}) using port {port}. Terminating...")
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except psutil.TimeoutExpired:
                        print(f"Process {pid} did not terminate gracefully. Killing...")
                        process.kill()
        return True
    except Exception as e:
        print(f"Error while killing process on port {port}: {e}")
        return False

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("0.0.0.0", port))
            return True
        except socket.error:
            return False

def start_prometheus_server(port):
    global prom_server
    if not check_port(port):
        print(f"Port {port} is already in use. Attempting to free it...")
        if not kill_process_using_port(port):
            print(f"Failed to free port {port}. Exiting.")
            sys.exit(1)
        if not check_port(port):
            print(f"Port {port} still in use after attempting to free it. Exiting.")
            sys.exit(1)
    print(f"Starting Prometheus server on port {port}")
    prom_server = prom.start_http_server(port)
    return True

def signal_handler(sig, frame, loop):
    print("Shutting down Prometheus server...")
    if prom_server:
        print("Cleaning up resources")
    loop.stop()
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    sys.exit(0)

# ---------------- Amarisoft API ----------------
async def amarisoft_api_request(target, msg):
    uri = "ws://" + target
    try:
        async with websockets.connect(uri, origin="Test") as websocket:
            ready = await websocket.recv()
            await websocket.send(msg)
            rsp = await websocket.recv()
            return json.loads(rsp)
    except Exception as e:
        print(f"EXCEPTION: Failed to connect to Amarisoft API at {uri}: {e}")
        return {"message": "ue_get", "ue_list": []}

# ---------------- Latency/Jitter Scraper ----------------
def scrape_latency_jitter():
    try:
        r = requests.get(LATENCY_DASHBOARD_URL, timeout=3)
        soup = BeautifulSoup(r.text, "html.parser")
        rows = soup.find_all("tr")[1:]  # skip header
        metrics = {}
        for row in rows:
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cols) < 4:
                continue
            interface = cols[1].lower()
            latency = float(cols[2])
            jitter = float(cols[3])
            if "uesimtun0" in interface:
                metrics["core_node"] = {"latency": latency, "jitter": jitter}
            elif "uesimtun1" in interface:
                metrics["mec_node"] = {"latency": latency, "jitter": jitter}
        return metrics
    except Exception as e:
        print(f"Error scraping latency dashboard: {e}")
        return {}

# ---------------- Node Metrics ----------------
async def fetch_metrics(node, latency_jitter_data=None):
    try:
        cpu_expr = f"avg(100 - ((rate(node_cpu_seconds_total{{job=\"node-exporter\",instance=\"{node['ip']}\",mode=\"idle\"}}[1m])) * 100))"
        mem_expr = f"100 - (avg(node_memory_MemAvailable_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) / avg(node_memory_MemTotal_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) * 100)"
        tx_expr = f"rate(node_network_transmit_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        rx_expr = f"rate(node_network_receive_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"

        response = {
            "cpu": float(requests.get(PROMETHEUS_URL, params={"query": cpu_expr}).json()["data"]["result"][0]["value"][1]),
            "memory": float(requests.get(PROMETHEUS_URL, params={"query": mem_expr}).json()["data"]["result"][0]["value"][1]),
            "tx": float(requests.get(PROMETHEUS_URL, params={"query": tx_expr}).json()["data"]["result"][0]["value"][1]),
            "rx": float(requests.get(PROMETHEUS_URL, params={"query": rx_expr}).json()["data"]["result"][0]["value"][1]),
            "cost": 4.0,
            "latency": 0.0,
            "jitter": 0.0
        }

        if latency_jitter_data and node['name'] in latency_jitter_data:
            response['latency'] = latency_jitter_data[node['name']]['latency']
            response['jitter'] = latency_jitter_data[node['name']]['jitter']

        LATENCY_GAUGE.labels(node=node['name']).set(response['latency'])
        JITTER_GAUGE.labels(node=node['name']).set(response['jitter'])

        return {node["name"]: response}
    except Exception as e:
        print(f"Error fetching metrics for {node['name']}: {e}")
        return {node["name"]: {"cpu": 0, "memory": 0, "tx": 0, "rx": 0, "latency": 0, "jitter": 0, "cost": 0}}

# ---------------- Amarisoft Prometheus ----------------
def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)
    num_ues_registered = len(json_gnb_ueget['ue_list'])
    if num_ues_registered == 0:
        return
    for ue_ix in range(num_ues_registered):
        ue_id = str(num_ues_registered - ue_ix)
        cells = json_gnb_ueget['ue_list'][ue_ix].get('cells', [{}])
        if not cells or not isinstance(cells, list) or len(cells) == 0:
            continue
        cell = cells[0]
        AMARISOFT_CQI_GAUGE.labels(ue=str(ue_id)).set(cell.get('cqi', 0))
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=str(ue_id)).set(cell.get('dl_bitrate', 0))
        AMARISOFT_DL_MCS_GAUGE.labels(ue=str(ue_id)).set(cell.get('dl_mcs', 0))
        AMARISOFT_EPRE_GAUGE.labels(ue=str(ue_id)).set(cell.get('epre', 0))
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=str(ue_id)).set(cell.get('pusch_snr', 0))
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=str(ue_id)).set(cell.get('ul_bitrate', 0))
        AMARISOFT_UL_MCS_GAUGE.labels(ue=str(ue_id)).set(cell.get('ul_mcs', 0))
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=str(ue_id)).set(cell.get('ul_path_loss', 0))

# ---------------- CSV Helper ----------------
def append_to_csv(file_path, row):
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

# ---------------- Process Metrics ----------------
async def process_metrics(json_gnb_ueget, node_metrics, now):
    row = {col: 0.0 for col in CSV_COLUMNS}
    row['timestamp'] = now.timestamp()

    # Node metrics
    nodes_output = {}
    for node in node_metrics:
        node_name = list(node.keys())[0]
        data = node[node_name]
        nodes_output[node_name] = data
        for k, v in data.items():
            row[f'{node_name}_{k}'] = float(v)

    # UE metrics
    ue_list = json_gnb_ueget.get('ue_list', [])
    ue_output = []
    if ue_list:
        ue_list_sorted = sorted(ue_list, key=lambda x: int(x.get('ue_id', 0)))
        for i, ue in enumerate(ue_list_sorted):
            if i >= MAX_UES:
                break
            cells = ue.get('cells', [{}])[0]
            ue_metrics = {
                "ue_id": i+1,
                "cqi": cells.get('cqi', 0.0),
                "dl_bitrate": cells.get('dl_bitrate', 0.0),
                "dl_mcs": cells.get('dl_mcs', 0.0),
                "epre": cells.get('epre', 0.0),
                "pusch_snr": cells.get('pusch_snr', 0.0),
                "ul_bitrate": cells.get('ul_bitrate', 0.0),
                "ul_mcs": cells.get('ul_mcs', 0.0),
                "ul_path_loss": cells.get('ul_path_loss', 0.0)
            }
            ue_output.append(ue_metrics)
            for k, v in ue_metrics.items():
                if k != "ue_id":
                    row[f'ue{i+1}_{k}'] = v

    # Print live JSON to screen
    combined_output = {
        "timestamp": now.isoformat(),
        "nodes": nodes_output,
        "ues": ue_output
    }
    print(json.dumps(combined_output, indent=4))

    # Append to CSV
    append_to_csv(ALL_CSV_FILE, row)
    daily_file = f"daily_metrics_{now.strftime('%Y-%m-%d')}.csv"
    append_to_csv(daily_file, row)

# ---------------- Main Loop ----------------
async def main():
    print("Starting combined metrics collection with latency/jitter")
    start_prometheus_server(PROMETHEUS_SERVER)

    if not os.path.exists(ALL_CSV_FILE):
        with open(ALL_CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, partial(signal_handler, sig, None, loop))

    requests_sent = 0
    start_time = time.time()
    duration = 4 * 24 * 3600  # 4 days

    while time.time() - start_time < duration:
        requests_sent += 1
        now = datetime.now()
        latency_jitter_data = scrape_latency_jitter()
        json_gnb_ueget = await amarisoft_api_request(TARGET_ENB, API_MESSAGE_ENB_UEGET)
        node_metrics = await asyncio.gather(*(fetch_metrics(node, latency_jitter_data) for node in NODES))

        expose_prometheus_metrics(requests_sent, json_gnb_ueget)
        await process_metrics(json_gnb_ueget, node_metrics, now)

        await asyncio.sleep(INTERVAL)

    print("Completed 4 days of data collection.")

# ---------------- Entry Point ----------------
if __name__ == "__main__":
    asyncio.run(main())

