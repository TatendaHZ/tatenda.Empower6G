#!/usr/bin/env python3
import asyncio
import websockets
import json
import requests
import time
from datetime import datetime
import prometheus_client as prom
import psutil
import socket
import signal
import sys
from functools import partial

# ------------------ Configuration ------------------
LOCAL = True
INTERVAL = 5
PROMETHEUS_NODE_IP = "192.168.2.6"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
OUTPUT_FILE = "metrics.svc"
PROMETHEUS_SERVER = 80

TARGET_ENB = "192.168.88.53:9001" if LOCAL else str(os.environ.get("TARGET_ENB"))

NODES = [
    {"name": "core node", "ip": "192.168.88.38:9100"},
    {"name": "mec node", "ip": "192.168.88.27:9100"},
    {"name": "kube-app-server", "ip": "192.168.88.40:9100"}
]

API_MESSAGE_ENB_UEGET = '{"message":"ue_get","stats": true}'

# ------------------ Prometheus Metrics ------------------
AMARISOFT_COUNTER = prom.Gauge('amarisoft_requests_total', 'Number of requests to gNB')
AMARISOFT_CQI_GAUGE = prom.Gauge('amarisoft_cqi', 'Channel Quality Indicator (CQI)', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('amarisoft_dl_bitrate', 'DL bitrate (Mbps)', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('amarisoft_dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('amarisoft_epre', 'Energy per resource element (dBm)', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('amarisoft_pusch_snr', 'PUSCH SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('amarisoft_ul_bitrate', 'UL bitrate (Mbps)', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('amarisoft_ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('amarisoft_ul_path_loss', 'UL path loss (dB)', ["ue"])

prom_server = None

# ------------------ Helper Functions ------------------
def kill_process_using_port(port):
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid:
                    psutil.Process(pid).terminate()
        return True
    except Exception as e:
        print(f"[WARN] Error killing process on port {port}: {e}")
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
        print(f"[INFO] Port {port} in use, attempting to free it...")
        kill_process_using_port(port)
        if not check_port(port):
            print(f"[ERROR] Port {port} still busy. Exiting.")
            sys.exit(1)
    print(f"[INFO] Starting Prometheus server on port {port}")
    prom_server = prom.start_http_server(port)

async def amarisoft_api_request(target, msg):
    uri = f"ws://{target}"
    try:
        async with websockets.connect(uri, origin="PrometheusRAN") as ws:
            await ws.recv()
            await ws.send(msg)
            rsp = await ws.recv()
            return json.loads(rsp)
    except Exception as e:
        print(f"[WARN] gNB API request failed: {e}")
        return {"message": "ue_get", "ue_list": []}

async def fetch_metrics(node):
    try:
        metrics = {}
        queries = {
            "cpu": f"100 - (avg(node_cpu_seconds_total{{instance='{node['ip']}',mode='idle'}}) * 100)",
            "memory": f"100 - (avg(node_memory_MemAvailable_bytes{{instance='{node['ip']}'}})/avg(node_memory_MemTotal_bytes{{instance='{node['ip']}'}}) * 100)",
            "tx": f"rate(node_network_transmit_bytes_total{{instance='{node['ip']}',device='enp0s3'}}[1m]) * 8",
            "rx": f"rate(node_network_receive_bytes_total{{instance='{node['ip']}',device='enp0s3'}}[1m]) * 8"
        }
        for key, q in queries.items():
            resp = requests.get(PROMETHEUS_URL, params={"query": q}).json()
            value = resp.get("data", {}).get("result", [])
            metrics[key] = float(value[0]["value"][1]) if value else 0
        metrics.update({"latency": 1.0, "cost": 4})
        return {node["name"]: metrics}
    except Exception as e:
        print(f"[WARN] Failed fetching node metrics for {node['name']}: {e}")
        return {node["name"]: {"cpu":0,"memory":0,"tx":0,"rx":0,"latency":0,"cost":0}}

def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)
    for ue_ix, ue in enumerate(json_gnb_ueget.get("ue_list", []), 1):
        cell = ue["cells"][0]
        ue_id = str(ue_ix)
        AMARISOFT_CQI_GAUGE.labels(ue=ue_id).set(cell.get("cqi",0))
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get("dl_bitrate",0))
        AMARISOFT_DL_MCS_GAUGE.labels(ue=ue_id).set(cell.get("dl_mcs",0))
        AMARISOFT_EPRE_GAUGE.labels(ue=ue_id).set(cell.get("epre",0))
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=ue_id).set(cell.get("pusch_snr",0))
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get("ul_bitrate",0))
        AMARISOFT_UL_MCS_GAUGE.labels(ue=ue_id).set(cell.get("ul_mcs",0))
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=ue_id).set(cell.get("ul_path_loss",0))

async def write_metrics(json_gnb_ueget, node_metrics, now):
    ran_metrics = {"time": now.timestamp(), "ue_list": []}
    for ue_ix, ue in enumerate(json_gnb_ueget.get("ue_list", []), 1):
        ue_data = ue.copy()
        ue_data["ue_id"] = str(ue_ix)
        ran_metrics["ue_list"].append(ue_data)
    dump = {
        "time": now.timestamp(),
        "ran_metrics": ran_metrics,
        "node_metrics": [nm for nm in node_metrics]
    }
    with open(OUTPUT_FILE, "w") as f:
        json.dump(dump, f, indent=4)

def signal_handler(sig, frame, loop):
    print("[INFO] Shutting down...")
    loop.stop()
    sys.exit(0)

# ------------------ Main ------------------
async def main():
    print("[INFO] Starting combined metrics collection")
    start_prometheus_server(PROMETHEUS_SERVER)
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
        await write_metrics(json_gnb_ueget, node_metrics, now)
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
