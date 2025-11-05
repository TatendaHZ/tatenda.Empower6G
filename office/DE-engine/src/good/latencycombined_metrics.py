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
from bs4 import BeautifulSoup

# ------------------ Configuration ------------------
INTERVAL = 5  # seconds
PROMETHEUS_NODE_IP = "192.168.88.40"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
OUTPUT_FILE = "metrics.svc"
PROMETHEUS_SERVER = 8000  # avoid sudo

LATENCY_DASHBOARD_URL = "http://192.168.88.46/"

LOCAL = True
if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"
else:
    import os
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))

NODES = [
    {"name": "core node", "ip": "192.168.88.38:9100"},
    {"name": "mec node", "ip": "192.168.88.27:9100"},
    {"name": "kube-app-server", "ip": "192.168.88.40:9100"}
]

# ------------------ Prometheus Gauges ------------------
AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'Channel quality indicator (CQI)', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate in Mbps', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'Energy per resource element (EPRE) in dBm', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'PUSCH SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate in Mbps', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL path Loss (PUSCH) SNR in dB', ["ue"])

prom_server = None

# ------------------ Functions ------------------
def kill_process_using_port(port):
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid:
                    process = psutil.Process(pid)
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except psutil.TimeoutExpired:
                        process.kill()
        return True
    except Exception as e:
        print(f"Error killing port {port}: {e}")
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
    prom_server = prom.start_http_server(port)
    return True

def signal_handler(sig, frame, loop):
    loop.stop()
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    sys.exit(0)

async def amarisoft_api_request(target, msg):
    uri = f"ws://{target}"
    try:
        async with websockets.connect(uri, origin="Test") as ws:
            await ws.recv()
            await ws.send(msg)
            rsp = await ws.recv()
            return json.loads(rsp)
    except Exception as e:
        print(f"Amarisoft API error: {e}")
        return {"message": "ue_get", "ue_list": []}

def scrape_latency_jitter():
    try:
        r = requests.get(LATENCY_DASHBOARD_URL, timeout=3)
        soup = BeautifulSoup(r.text, "html.parser")
        rows = soup.find_all("tr")[1:]
        metrics = {}
        for row in rows:
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cols) < 4: continue
            interface = cols[1].lower()
            latency = float(cols[2])
            jitter = float(cols[3])
            if "uesimtun0" in interface:
                metrics["core node"] = {"latency": latency, "jitter": jitter}
            elif "uesimtun1" in interface:
                metrics["mec node"] = {"latency": latency, "jitter": jitter}
        return metrics
    except Exception as e:
        print(f"Latency scrape error: {e}")
        return {}

async def fetch_metrics(node, latency_jitter_data):
    try:
        cpu_expr = f"avg(100 - ((rate(node_cpu_seconds_total{{job=\"node-exporter\",instance=\"{node['ip']}\",mode=\"idle\"}}[1m])) * 100))"
        mem_expr = f"100 - (avg(node_memory_MemAvailable_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) / avg(node_memory_MemTotal_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) * 100)"
        tx_expr = f"rate(node_network_transmit_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        rx_expr = f"rate(node_network_receive_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"

        result = {
            "cpu": requests.get(PROMETHEUS_URL, params={"query": cpu_expr}).json()["data"]["result"][0]["value"][1],
            "memory": requests.get(PROMETHEUS_URL, params={"query": mem_expr}).json()["data"]["result"][0]["value"][1],
            "tx": requests.get(PROMETHEUS_URL, params={"query": tx_expr}).json()["data"]["result"][0]["value"][1],
            "rx": requests.get(PROMETHEUS_URL, params={"query": rx_expr}).json()["data"]["result"][0]["value"][1],
            "cost": "4"
        }

        node_name = node["name"]
        if node_name in latency_jitter_data:
            result["latency"] = latency_jitter_data[node_name]["latency"]
            result["jitter"] = latency_jitter_data[node_name]["jitter"]
        else:
            result["latency"] = 0
            result["jitter"] = 0
        return {node_name: result}
    except Exception as e:
        print(f"Node metrics error: {e}")
        return {node["name"]: {"cpu": 0, "memory": 0, "tx": 0, "rx": 0, "latency": 0, "jitter": 0, "cost": 0}}

def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)
    for ue_ix, ue in enumerate(json_gnb_ueget.get("ue_list", [])):
        ue_id = str(len(json_gnb_ueget['ue_list']) - ue_ix)
        cell = ue['cells'][0]
        AMARISOFT_CQI_GAUGE.labels(ue=ue_id).set(cell.get('cqi', 0))
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get('dl_bitrate', 0))
        AMARISOFT_DL_MCS_GAUGE.labels(ue=ue_id).set(cell.get('dl_mcs', 0))
        AMARISOFT_EPRE_GAUGE.labels(ue=ue_id).set(cell.get('epre', 0))
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=ue_id).set(cell.get('pusch_snr', 0))
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get('ul_bitrate', 0))
        AMARISOFT_UL_MCS_GAUGE.labels(ue=ue_id).set(cell.get('ul_mcs', 0))
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=ue_id).set(cell.get('ul_path_loss', 0))

async def write_metrics(json_gnb_ueget, node_metrics, now):
    ran_metrics = {'time': now.timestamp(), 'ue_list': []}
    for ue_ix, ue in enumerate(json_gnb_ueget.get('ue_list', [])):
        ue_copy = ue.copy()
        ue_copy['ue_id'] = str(len(json_gnb_ueget['ue_list']) - ue_ix)
        ran_metrics['ue_list'].append(ue_copy)

    dump = {
        "time": now.timestamp(),
        "ran_metrics": ran_metrics,
        "node_metrics": [nm for node in node_metrics for nm in [node]]
    }

    with open(OUTPUT_FILE, 'w') as f:
        f.write(json.dumps(dump, indent=4))

# ------------------ Main Loop ------------------
async def main():
    print("🚀 Starting combined metrics collection")

    start_prometheus_server(PROMETHEUS_SERVER)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, partial(signal_handler, sig, None, loop))

    requests_sent = 0
    while True:
        requests_sent += 1
        now = datetime.now()

        latency_jitter_data = scrape_latency_jitter()
        json_gnb_ueget = await amarisoft_api_request(TARGET_ENB, '{"message":"ue_get","stats": true}')
        node_metrics = await asyncio.gather(*(fetch_metrics(node, latency_jitter_data) for node in NODES))
        expose_prometheus_metrics(requests_sent, json_gnb_ueget)
        await write_metrics(json_gnb_ueget, node_metrics, now)

        with open(OUTPUT_FILE, 'r') as f:
            print(f.read())

        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
