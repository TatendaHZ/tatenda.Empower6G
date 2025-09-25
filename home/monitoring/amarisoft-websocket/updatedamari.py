import asyncio
import websockets
import time
import json
import pprint
import os
from datetime import datetime
import prometheus_client as prom
import logging

# Set LOCAL True for running locally
LOCAL = True

if LOCAL:
    # HARDCODED ENV variables (comment if using Dockerfile)
    TARGET_ENB = "192.168.88.53:9001"  # Amarisoft gNB (or eNB)
    TARGET_MME = "192.168.88.53:9000"  # Amarisoft AMF (or MME)
    INTERVAL = 5.0
    LOG = "amarisoft.log"
else:
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))
    TARGET_MME = str(os.environ.get("TARGET_MME"))
    INTERVAL = float(os.environ.get("INTERVAL"))
    LOG = str(os.environ.get("LOG"))

# Amarisoft API messages
API_MESSAGE_ENB_UEGET = '{"message":"ue_get","stats": true}'
API_MESSAGE_MME_UEGET = '{"message":"ue_get"}'

# Prometheus metrics
AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_CQI_GAUGE = prom.Gauge('cqi', 'Channel quality indicator (CQI)', ["ue"])
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate in Mbps', ["ue"])
AMARISOFT_DL_MCS_GAUGE = prom.Gauge('dl_mcs', 'DL MCS', ["ue"])
AMARISOFT_EPRE_GAUGE = prom.Gauge('epre', 'EPRE in dBm', ["ue"])
AMARISOFT_PUSCH_SNR_GAUGE = prom.Gauge('pusch_snr', 'PUSCH SNR', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate in Mbps', ["ue"])
AMARISOFT_UL_MCS_GAUGE = prom.Gauge('ul_mcs', 'UL MCS', ["ue"])
AMARISOFT_UL_PATHLOSS_GAUGE = prom.Gauge('ul_path_loss', 'UL Path Loss in dB', ["ue"])

PROMETHEUS_SERVER = 80
pp = pprint.PrettyPrinter(indent=4)

async def amarisoft_api_request(target, msg):
    uri = "ws://" + target
    print("Requesting to API uri:", uri)
    async with websockets.connect(uri, origin="Test") as websocket:
        await websocket.recv()
        await websocket.send(msg)
        rsp = await websocket.recv()
        return json.loads(rsp)

def write_log(json_response: dict, now: datetime):
    dump = {'time': now.timestamp(), 'ue_list': json_response.get('ue_list', [])}
    with open(LOG, 'w') as output:
        output.write(json.dumps(dump))

def expose_prometheus_metrics(requests_sent, json_gnb_ueget):
    AMARISOFT_COUNTER.set(requests_sent)

    ue_list = json_gnb_ueget.get("ue_list", [])
    if not ue_list:
        print("No UEs found. Setting all gauges to 0.")
        dummy_ue = "none"
        AMARISOFT_CQI_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_DL_MCS_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_EPRE_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_UL_MCS_GAUGE.labels(ue=dummy_ue).set(0)
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=dummy_ue).set(0)
        return

    for ue_ix, ue in enumerate(ue_list):
        ue_id = str(ue.get("rnti", ue_ix + 1))
        cell = ue.get("cells", [{}])[0]

        cqi = cell.get("cqi", 0)
        AMARISOFT_CQI_GAUGE.labels(ue=ue_id).set(cqi)

        dl_bitrate = cell.get("dl_bitrate", 0)
        AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_id).set(dl_bitrate)

        dl_mcs = cell.get("dl_mcs", 0)
        AMARISOFT_DL_MCS_GAUGE.labels(ue=ue_id).set(dl_mcs)

        epre = cell.get("epre", 0)
        AMARISOFT_EPRE_GAUGE.labels(ue=ue_id).set(epre)

        pusch_snr = cell.get("pusch_snr", 0)
        AMARISOFT_PUSCH_SNR_GAUGE.labels(ue=ue_id).set(pusch_snr)

        ul_bitrate = cell.get("ul_bitrate", 0)
        AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_id).set(ul_bitrate)

        ul_mcs = cell.get("ul_mcs", 0)
        AMARISOFT_UL_MCS_GAUGE.labels(ue=ue_id).set(ul_mcs)

        ul_path_loss = cell.get("ul_path_loss", 0)
        AMARISOFT_UL_PATHLOSS_GAUGE.labels(ue=ue_id).set(ul_path_loss)

        print(f"UE {ue_id} - CQI: {cqi}, DL bitrate: {dl_bitrate}, UL bitrate: {ul_bitrate}")

def main():
    print("Starting Amarisoft Prometheus Exporter on port", PROMETHEUS_SERVER)
    prom.start_http_server(PROMETHEUS_SERVER)

    requests_sent = 0

    while True:
        print("Polling Amarisoft Callbox")
        requests_sent += 1
        now = datetime.now()

        json_gnb_ueget = None
        while json_gnb_ueget is None:
            try:
                json_gnb_ueget = asyncio.run(amarisoft_api_request(TARGET_ENB, API_MESSAGE_ENB_UEGET))
            except Exception as e:
                print(f"[ERROR] Failed to connect to Amarisoft API: {e}")
                time.sleep(INTERVAL)

        pp.pprint(json_gnb_ueget)
        write_log(json_gnb_ueget, now)
        expose_prometheus_metrics(requests_sent, json_gnb_ueget)
        time.sleep(INTERVAL)
        print("\n\n")

if __name__ == "__main__":
    main()
