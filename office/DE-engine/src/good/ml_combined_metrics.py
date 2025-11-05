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
import os
import csv
import pandas as pd
import numpy as np
from functools import partial
import statistics

# --- Configuration ---
LOCAL = True
INTERVAL = 5  # seconds
PROMETHEUS_NODE_IP = "192.168.88.40"
PROMETHEUS_PORT = "30041"
PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"
PROMETHEUS_SERVER_PORT = 80
DATA_DIR = "autoencoder_data"
ML_CSV_FILE = os.path.join(DATA_DIR, "ml_metrics.csv")

if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"
else:
    TARGET_ENB = os.environ.get("TARGET_ENB")

NODES = [
    {"name": "core_node", "ip": "192.168.88.38:9100"},
    {"name": "mec_node", "ip": "192.168.88.27:9100"},
    {"name": "kube_app_server", "ip": "192.168.88.40:9100"}
]

API_MESSAGE_ENB_UEGET = '{"message":"ue_get","stats": true}'

# --- Prometheus metrics ---
AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'CQI', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate Mbps', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'EPRE dBm', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'PUSCH SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate Mbps', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL path loss dB', ["ue"])

# --- Globals ---
prom_server = None
feature_columns = None

# --- Functions ---
def setup_directories():
    os.makedirs(DATA_DIR, exist_ok=True)

def initialize_feature_columns():
    global feature_columns
    feature_columns = [
        'core_node_cpu', 'core_node_memory', 'core_node_tx', 'core_node_rx', 'core_node_latency', 'core_node_cost',
        'mec_node_cpu', 'mec_node_memory', 'mec_node_tx', 'mec_node_rx', 'mec_node_latency', 'mec_node_cost',
        'kube_app_server_cpu', 'kube_app_server_memory', 'kube_app_server_tx', 'kube_app_server_rx', 'kube_app_server_latency', 'kube_app_server_cost',
        'ue_count', 'avg_cqi', 'avg_dl_bitrate', 'avg_ul_bitrate', 'avg_dl_mcs', 'avg_ul_mcs',
        'avg_epre', 'avg_pusch_snr', 'avg_ul_path_loss', 'max_cqi', 'min_cqi', 'cqi_std',
        'network_load', 'system_health', 'resource_utilization'
    ]
    with open(os.path.join(DATA_DIR, "feature_columns.json"), 'w') as f:
        json.dump(feature_columns, f, indent=2)
    with open(ML_CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp'] + feature_columns)
    print(f"Initialized ML CSV file: {ML_CSV_FILE}")

def kill_process_using_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
            pid = conn.pid
            if pid:
                p = psutil.Process(pid)
                print(f"Killing process {pid} on port {port}")
                p.terminate()
                try: p.wait(timeout=3)
                except psutil.TimeoutExpired: p.kill()
    return True

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
    print(f"Prometheus server started on port {port}")

def signal_handler(sig, frame, loop):
    print("Shutting down gracefully...")
    create_normalized_dataset()
    loop.stop()
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    sys.exit(0)

async def amarisoft_api_request(target, msg, retries=3):
    uri = f"ws://{target}"
    for attempt in range(retries):
        try:
            async with websockets.connect(uri, origin="Test") as ws:
                await ws.recv()
                await ws.send(msg)
                rsp = await ws.recv()
                return json.loads(rsp)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            await asyncio.sleep(1)
    return {"message": "ue_get", "ue_list": []}

async def fetch_metrics(node):
    try:
        cpu_expr = f"avg(100 - ((rate(node_cpu_seconds_total{{job=\"node-exporter\",instance=\"{node['ip']}\",mode=\"idle\"}}[1m])) * 100))"
        mem_expr = f"100 - (avg(node_memory_MemAvailable_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) / avg(node_memory_MemTotal_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) * 100)"
        tx_expr = f"rate(node_network_transmit_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        rx_expr = f"rate(node_network_receive_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        vals = {}
        for expr, key in [(cpu_expr,'cpu'),(mem_expr,'memory'),(tx_expr,'tx'),(rx_expr,'rx')]:
            try:
                resp = requests.get(PROMETHEUS_URL, params={"query": expr}, timeout=3).json()
                vals[key] = float(resp["data"]["result"][0]["value"][1])
            except: vals[key] = 0.0
        vals.update({"latency":1.0, "cost":4.0})
        return {node["name"]: vals}
    except Exception as e:
        print(f"Error fetching {node['name']}: {e}")
        return {node["name"]: {"cpu":0,"memory":0,"tx":0,"rx":0,"latency":0,"cost":0}}

def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)
    for ue_ix, ue in enumerate(json_gnb_ueget.get('ue_list', [])):
        ue_id = str(len(json_gnb_ueget['ue_list']) - ue_ix)
        cell = ue.get('cells',[{}])[0]
        AMARISOFT_CQI_GAUGE.labels(ue=ue_id).set(cell.get('cqi',0))
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get('dl_bitrate',0))
        AMARISOFT_DL_MCS_GAUGE.labels(ue=ue_id).set(cell.get('dl_mcs',0))
        AMARISOFT_EPRE_GAUGE.labels(ue=ue_id).set(cell.get('epre',0))
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=ue_id).set(cell.get('pusch_snr',0))
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_id).set(cell.get('ul_bitrate',0))
        AMARISOFT_UL_MCS_GAUGE.labels(ue=ue_id).set(cell.get('ul_mcs',0))
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=ue_id).set(cell.get('ul_path_loss',0))

def create_ml_features(ran_metrics, node_metrics):
    features = {}
    # Node metrics
    for node_dict in node_metrics:
        for name, metrics in node_dict.items():
            for k,v in metrics.items():
                features[f"{name}_{k}"] = v
    # RAN metrics
    ue_list = ran_metrics.get('ue_list',[])
    features['ue_count'] = len(ue_list)
    if ue_list:
        cqi_values = [ue.get('cells',[{}])[0].get('cqi',0) for ue in ue_list]
        dl_bitrate = [ue.get('cells',[{}])[0].get('dl_bitrate',0) for ue in ue_list]
        ul_bitrate = [ue.get('cells',[{}])[0].get('ul_bitrate',0) for ue in ue_list]
        dl_mcs = [ue.get('cells',[{}])[0].get('dl_mcs',0) for ue in ue_list]
        ul_mcs = [ue.get('cells',[{}])[0].get('ul_mcs',0) for ue in ue_list]
        epre = [ue.get('cells',[{}])[0].get('epre',0) for ue in ue_list]
        snr = [ue.get('cells',[{}])[0].get('pusch_snr',0) for ue in ue_list]
        pathloss = [ue.get('cells',[{}])[0].get('ul_path_loss',0) for ue in ue_list]

        features.update({
            'avg_cqi': statistics.mean(cqi_values),
            'avg_dl_bitrate': statistics.mean(dl_bitrate),
            'avg_ul_bitrate': statistics.mean(ul_bitrate),
            'avg_dl_mcs': statistics.mean(dl_mcs),
            'avg_ul_mcs': statistics.mean(ul_mcs),
            'avg_epre': statistics.mean(epre),
            'avg_pusch_snr': statistics.mean(snr),
            'avg_ul_path_loss': statistics.mean(pathloss),
            'max_cqi': max(cqi_values),
            'min_cqi': min(cqi_values),
            'cqi_std': statistics.stdev(cqi_values) if len(cqi_values)>1 else 0
        })
    else:
        for k in ['avg_cqi','avg_dl_bitrate','avg_ul_bitrate','avg_dl_mcs','avg_ul_mcs',
                  'avg_epre','avg_pusch_snr','avg_ul_path_loss','max_cqi','min_cqi','cqi_std']:
            features[k] = 0.0

    # Composite metrics
    features['network_load'] = (features.get('core_node_tx',0)+features.get('core_node_rx',0))/1e6
    features['system_health'] = statistics.mean([features.get('core_node_cpu',0),features.get('mec_node_cpu',0),features.get('kube_app_server_cpu',0)])
    features['resource_utilization'] = statistics.mean([features.get('core_node_memory',0),features.get('mec_node_memory',0),features.get('kube_app_server_memory',0)])

    return features

def create_normalized_dataset():
    if not os.path.exists(ML_CSV_FILE):
        return
    df = pd.read_csv(ML_CSV_FILE)
    if len(df)==0:
        return
    normalized_file = os.path.join(DATA_DIR, "normalized_metrics.csv")
    feature_cols = [c for c in df.columns if c!='timestamp']
    df_norm = df.copy()
    for col in feature_cols:
        df_norm[col] = (df[col]-df[col].mean())/df[col].std() if df[col].std()>0 else 0
    df_norm.to_csv(normalized_file,index=False,float_format='%.6f')
    print(f"Normalized dataset saved: {normalized_file}")

async def write_ml_metrics(json_gnb_ueget, node_metrics, now):
    ran_metrics = {'time': now.timestamp(), 'ue_list': []}
    for ue_ix, ue in enumerate(json_gnb_ueget.get('ue_list',[])):
        ue_copy = ue.copy()
        ue_copy['ue_id'] = str(len(json_gnb_ueget['ue_list'])-ue_ix)
        ran_metrics['ue_list'].append(ue_copy)
    features = create_ml_features(ran_metrics, node_metrics)
    row = [now.timestamp()] + [features.get(col,0.0) for col in feature_columns]
    with open(ML_CSV_FILE,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print(f"Sample {len(pd.read_csv(ML_CSV_FILE))} written to CSV")

# --- Main loop ---
async def main():
    print("Starting ML metrics collection...")
    setup_directories()
    initialize_feature_columns()
    start_prometheus_server(PROMETHEUS_SERVER_PORT)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, partial(signal_handler, sig, None, loop))

    requests_sent = 0
    while True:
        requests_sent += 1
        print(f"\n- Sample {requests_sent}")
        now = datetime.now()
        json_gnb_ueget = await amarisoft_api_request(TARGET_ENB, API_MESSAGE_ENB_UEGET)
        node_metrics = await asyncio.gather(*(fetch_metrics(n) for n in NODES))
        expose_prometheus_metrics(requests_sent, json_gnb_ueget)
        await write_ml_metrics(json_gnb_ueget, node_metrics, now)
        if requests_sent % 100 == 0:
            create_normalized_dataset()
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
