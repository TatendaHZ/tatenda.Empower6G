import asyncio
import websockets
import json
import requests
from datetime import datetime
import prometheus_client as prom
import psutil
import socket
import signal
import sys
from functools import partial
import os
import csv

# ---------------- Configuration ----------------
LOCAL = True
INTERVAL = 5  # seconds
PROMETHEUS_NODE_IP = "192.168.88.40"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
PROMETHEUS_SERVER = 80
OUTPUT_FILE = "metrics.svc"
DAILY_DIR = "./daily_metrics"
COMBINED_FILE = "combined_4days.csv"

os.makedirs(DAILY_DIR, exist_ok=True)

if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"
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
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'CQI', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'EPRE', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'PUSCH SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL path loss', ["ue"])

prom_server = None

# ---------------- Helper Functions ----------------
def kill_process_using_port(port):
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid:
                    process = psutil.Process(pid)
                    print(f"Killing process {pid} ({process.name()}) using port {port}")
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except psutil.TimeoutExpired:
                        process.kill()
        return True
    except Exception as e:
        print(f"Error killing process: {e}")
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
        kill_process_using_port(port)
        if not check_port(port):
            print(f"Port {port} still in use. Exiting.")
            sys.exit(1)
    print(f"Starting Prometheus server on port {port}")
    prom_server = prom.start_http_server(port)
    return True

def signal_handler(sig, frame, loop):
    print("Shutting down Prometheus server...")
    loop.stop()
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    sys.exit(0)

async def amarisoft_api_request(target, msg):
    uri = f"ws://{target}"
    try:
        async with websockets.connect(uri, origin="Test") as websocket:
            await websocket.recv()
            await websocket.send(msg)
            rsp = await websocket.recv()
            return json.loads(rsp)
    except Exception as e:
        print(f"Failed to connect to Amarisoft API: {e}")
        return {"message": "ue_get", "ue_list": []}

async def fetch_metrics(node):
    try:
        cpu_expr = f"avg(100 - ((rate(node_cpu_seconds_total{{job=\"node-exporter\",instance=\"{node['ip']}\",mode=\"idle\"}}[1m])) * 100))"
        mem_expr = f"100 - (avg(node_memory_MemAvailable_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) / avg(node_memory_MemTotal_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) * 100)"
        tx_expr = f"rate(node_network_transmit_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        rx_expr = f"rate(node_network_receive_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"

        response = {
            "cpu": requests.get(PROMETHEUS_URL, params={"query": cpu_expr}).json()["data"]["result"][0]["value"][1],
            "memory": requests.get(PROMETHEUS_URL, params={"query": mem_expr}).json()["data"]["result"][0]["value"][1],
            "tx": requests.get(PROMETHEUS_URL, params={"query": tx_expr}).json()["data"]["result"][0]["value"][1],
            "rx": requests.get(PROMETHEUS_URL, params={"query": rx_expr}).json()["data"]["result"][0]["value"][1],
            "latency": "1.0",
            "cost": "4"
        }
        return {node["name"]: response}
    except Exception as e:
        print(f"Error fetching metrics for {node['name']}: {e}")
        return {node["name"]: {"cpu": 0, "memory": 0, "tx": 0, "rx": 0, "latency": 0, "cost": 0}}

def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)
    for idx, ue in enumerate(json_gnb_ueget.get('ue_list', [])):
        ue_id = str(idx + 1)
        AMARISOFT_CQI_GAUGE.labels(ue=ue_id).set(ue['cells'][0]['cqi'])
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_id).set(ue['cells'][0]['dl_bitrate'])
        AMARISOFT_DL_MCS_GAUGE.labels(ue=ue_id).set(ue['cells'][0].get('dl_mcs', 0))
        AMARISOFT_EPRE_GAUGE.labels(ue=ue_id).set(ue['cells'][0]['epre'])
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=ue_id).set(ue['cells'][0]['pusch_snr'])
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_id).set(ue['cells'][0]['ul_bitrate'])
        AMARISOFT_UL_MCS_GAUGE.labels(ue=ue_id).set(ue['cells'][0].get('ul_mcs', 0))
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=ue_id).set(ue['cells'][0].get('ul_path_loss', 0))

def save_csv_and_print(now, json_gnb_ueget, node_metrics):
    date_str = now.strftime("%Y-%m-%d")
    daily_file = os.path.join(DAILY_DIR, f"metrics_{date_str}.csv")

    headers = [
        "timestamp",
        *[f"{node}_{metric}" for node in ["core_node","mec_node","kube_app_server"] for metric in ["cpu","memory","tx","rx","latency","cost"]],
        "ue_count",
        "ue_ids"
    ]

    ue_list = json_gnb_ueget.get('ue_list', [])
    ue_count = len(ue_list)
    ue_ids = [str(idx+1) for idx in range(ue_count)]

    row = [now.timestamp()]
    for nm in ["core_node","mec_node","kube_app_server"]:
        metrics = node_metrics[[n for n in range(len(node_metrics)) if nm in node_metrics[n]][0]][nm]
        row.extend([metrics['cpu'], metrics['memory'], metrics['tx'], metrics['rx'], metrics['latency'], metrics['cost']])
    row.extend([ue_count, ",".join(ue_ids)])

    # Save daily CSV
    write_header = not os.path.exists(daily_file)
    with open(daily_file, 'a', newline='') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(headers)
        writer.writerow(row)

    # Save combined CSV
    write_header = not os.path.exists(COMBINED_FILE)
    with open(COMBINED_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(headers)
        writer.writerow(row)

    # ----------- PRINT FULL METRICS -----------
    print(f"\n[{now.strftime('%Y-%m-%d %H:%M:%S')}] Request metrics saved")
    print("------ Node Metrics ------")
    for node in node_metrics:
        for name, m in node.items():
            print(f"{name}: CPU={m['cpu']}%, MEM={m['memory']}%, TX={m['tx']}, RX={m['rx']}, Latency={m['latency']}, Cost={m['cost']}")
    print("------ UE Metrics ------")
    for idx, ue in enumerate(ue_list):
        print(f"UE{idx+1}: CQI={ue['cells'][0]['cqi']}, DL={ue['cells'][0]['dl_bitrate']} bps, UL={ue['cells'][0]['ul_bitrate']} bps, "
              f"DL MCS={ue['cells'][0].get('dl_mcs',0)}, UL MCS={ue['cells'][0].get('ul_mcs',0)}, EPRE={ue['cells'][0]['epre']}, "
              f"PUSCH SNR={ue['cells'][0]['pusch_snr']}, UL Path Loss={ue['cells'][0].get('ul_path_loss',0)}")

# ---------------- Main Loop ----------------
async def main():
    print("Starting combined metrics collection")
    if not start_prometheus_server(PROMETHEUS_SERVER):
        sys.exit(1)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, partial(signal_handler, sig, None, loop))

    requests_sent = 0
    while True:
        requests_sent += 1
        now = datetime.now()
        json_gnb_ueget = await amarisoft_api_request(TARGET_ENB, API_MESSAGE_ENB_UEGET)
        node_metrics = await asyncio.gather(*(fetch_metrics(node) for node in NODES))
        expose_prometheus_metrics(requests_sent, json_gnb_ueget)
        save_csv_and_print(now, json_gnb_ueget, node_metrics)
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())

