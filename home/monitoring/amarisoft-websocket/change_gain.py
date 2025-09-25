# -----------------------------------------------------------
# Iteratively requests the config of the gNB through a WebSocket and writes it in a file.
# -----------------------------------------------------------

import asyncio
import websockets   # Install locally through command pip install "websockets==8.1"
import time
import json
import pprint
import os
from datetime import datetime
import prometheus_client as prom

# Set LOCAL True for running locally
LOCAL = True

if LOCAL:
    # HARDCODED ENV variables (comment if using Dockerfile)
    TARGET_ENB = "10.1.14.249:9001"  # Socket for of Amarisoft gNB (or eNB)
    TARGET_MME = "10.1.14.249:9000" # Socket for of Amarisoft AMF (or MME)
    CELL_GAIN = "-8"
else:
    # ENV variables from Dockerfile
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))
    TARGET_MME = str(os.environ.get("TARGET_MME"))

# API_MESSAGE_CHANGE_GAIN = '{"message":"rf","tx_gain":[40,40,40,40]}'
#API_MESSAGE_CHANGE_GAIN = '{"message":"rf","tx_gain":[70,70,70,70]}'

#API_MESSAGE_CHANGE_GAIN = '{"message":"rf","rx_gain":[9,9,9,9]}'
#API_MESSAGE_CHANGE_GAIN = '{"message":"rf","rx_gain":[12,12,12,12]}'
#API_MESSAGE_CHANGE_GAIN = '{"message":"rf","rx_gain":[16,16,16,16]}'
API_MESSAGE_CHANGE_GAIN = '{"message":"rf","rx_gain":[20,20,20,20]}'

pp = pprint.PrettyPrinter(indent=4)

async def amarisoft_api_request(target, msg):
    uri = "ws://" + target

    print("Requesting to API uri: ", uri)

    async with websockets.connect(uri, origin="Test") as websocket:

        ready = await websocket.recv()
        await websocket.send(msg)   
        rsp = await websocket.recv()
        # pp.pprint(json.loads(rsp))

        return json.loads(rsp)

def main():

    print("Amarisoft change gain")
    print("Starting requests to Amarisoft Callbox")  
    now = datetime.now()

    requests_sent = 0
    json_gnb_ueget = None
    while json_gnb_ueget is None:
        try:
            # connect
            json_gnb_ueget = asyncio.run(amarisoft_api_request(TARGET_ENB, API_MESSAGE_CHANGE_GAIN))
            requests_sent += 1
            print("- request " + str(requests_sent))
        except:
            print("EXCEPTION: something went wrong when connecting to Amarisoft API. Retrying...")
    
    print("DONE!")

    pp.pprint(json_gnb_ueget)
 
    print("\n\n")

if __name__ == "__main__":
    main()
