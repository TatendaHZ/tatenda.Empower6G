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

# Configuration
LOCAL = True
INTERVAL = 30  # Data collection interval in seconds
PROMETHEUS_NODE_IP = "192.168.2.6"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
OUTPUT_FILE = "metrics.svc"  # Output file for combined metrics
PROMETHEUS_SERVER = 80  # Prometheus port

if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"  # Amarisoft gNB
    TARGET_MME = "192.168.88.53:9000"  # Amarisoft AMF (unused)
else:
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))
    TARGET_MME = str(os.environ.get("TARGET_MME"))

NODES = [
    {"name": "core node", "ip": "192.168.2.9:9100"},
    {"name": "mec node", "ip": "192.168.2.10:9100"},
    {"name": "kube-app-server", "ip": "192.168.2.6:9100"}
]

# Amarisoft API message
API_MESSAGE_ENB_UEGET = '{"message":"ue_get","stats": true}'

# Prometheus metrics for Amarisoft
AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'Channel quality indicator (CQI)', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate in Mbps', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'Energy per resource element (EPRE) in dBm', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'Physical uplink shared channel (PUSCH) SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate in Mbps', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL path Loss (PUSCH) SNR in dB', ["ue"])

# Global variable to track the Prometheus server
prom_server = None

def kill_process_using_port(port):
    """Find and kill processes using the specified port."""
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid:
                    process = psutil.Process(pid)
                    print(f"Found process {pid} ({process.name()}) using port {port}. Terminating...")
                    process.terminate()
                    try:
                        process.wait(timeout=3)  # Wait up to 3 seconds for graceful termination
                    except psutil.TimeoutExpired:
                        print(f"Process {pid} did not terminate gracefully. Killing...")
                        process.kill()
        return True
    except Exception as e:
        print(f"Error while killing process on port {port}: {e}")
        return False

def check_port(port):
    """Check if the port is available."""
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
        # Verify port is free after killing process
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

async def amarisoft_api_request(target, msg):
    uri = "ws://" + target
    print(f"Requesting to API uri: {uri}")
    try:
        async with websockets.connect(uri, origin="Test") as websocket:
            ready = await websocket.recv()
            await websocket.send(msg)
            rsp = await websocket.recv()
            return json.loads(rsp)
    except Exception as e:
        print(f"EXCEPTION: Failed to connect to Amarisoft API at {uri}: {e}")
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
    num_ues_registered = len(json_gnb_ueget['ue_list'])
    if num_ues_registered == 0:
        return
    for ue_ix in range(num_ues_registered):
        ue_id = str(num_ues_registered - ue_ix)
        cqi = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['cqi']
        AMARISOFT_CQI_GAUGE.labels(ue=str(ue_id)).set(cqi)
        dl_bitrate = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['dl_bitrate']
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=str(ue_id)).set(dl_bitrate)
        dl_mcs = json_gnb_ueget['ue_list'][ue_ix]['cells'][0].get('dl_mcs', 0)
        AMARISOFT_DL_MCS_GAUGE.labels(ue=str(ue_id)).set(dl_mcs)
        epre = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['epre']
        AMARISOFT_EPRE_GAUGE.labels(ue=str(ue_id)).set(epre)
        pusch_snr = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['pusch_snr']
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=str(ue_id)).set(pusch_snr)
        ul_bitrate = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['ul_bitrate']
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=str(ue_id)).set(ul_bitrate)
        ul_mcs = json_gnb_ueget['ue_list'][ue_ix]['cells'][0].get('ul_mcs', 0)
        AMARISOFT_UL_MCS_GAUGE.labels(ue=str(ue_id)).set(ul_mcs)
        ul_path_loss = json_gnb_ueget['ue_list'][ue_ix]['cells'][0]['ul_path_loss']
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=str(ue_id)).set(ul_path_loss)

async def write_metrics(json_gnb_ueget, node_metrics, now):
    dump = {
        "time": now.timestamp(),
        "ran_metrics": {"ue_list": json_gnb_ueget.get("ue_list", [])},
        "node_metrics": [value for node in node_metrics for value in [node]]
    }
    with open(OUTPUT_FILE, 'w') as output:
        output.write(json.dumps(dump, indent=4))
    output.close()

async def main():
    print("Starting combined metrics collection (Amarisoft + Prometheus)")
    
    # Start Prometheus server, killing any process using port 80
    if not start_prometheus_server(PROMETHEUS_SERVER):
        print(f"Failed to start Prometheus server on port {PROMETHEUS_SERVER}. Exiting.")
        sys.exit(1)

    # Set up signal handlers for graceful shutdown
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, partial(signal_handler, sig, None, loop))

    requests_sent = 0
    while True:
        requests_sent += 1
        print(f"\n- Request {requests_sent}")
        now = datetime.now()

        # Fetch Amarisoft gNB metrics (handle disconnection)
        json_gnb_ueget = await amarisoft_api_request(TARGET_ENB, API_MESSAGE_ENB_UEGET)

        # Fetch Prometheus node metrics
        node_metrics = await asyncio.gather(*(fetch_metrics(node) for node in NODES))

        # Expose Amarisoft metrics to Prometheus
        expose_prometheus_metrics(requests_sent, json_gnb_ueget)

        # Write combined metrics to .svc file
        await write_metrics(json_gnb_ueget, node_metrics, now)

        # Print combined metrics for debugging
        with open(OUTPUT_FILE, 'r') as f:
            print(f.read())

        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
