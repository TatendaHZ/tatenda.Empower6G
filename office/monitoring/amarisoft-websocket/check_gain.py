# -----------------------------------------------------------
# Requests the current RF configuration (tx_gain, rx_gain, etc.)
# from Amarisoft gNB through WebSocket.
# -----------------------------------------------------------

import asyncio
import websockets   # Install with: pip install "websockets==8.1"
import json
import pprint
import os
from datetime import datetime

# Set LOCAL True for running locally
LOCAL = True

if LOCAL:
    # HARDCODED ENV variables (comment out if using Dockerfile)
    TARGET_ENB = "192.168.88.53:9001"  # Socket for Amarisoft gNB (or eNB)
    TARGET_MME = "192.168.88.53:9000"  # Socket for Amarisoft AMF (or MME)
else:
    # ENV variables from Dockerfile
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))
    TARGET_MME = str(os.environ.get("TARGET_MME"))

# Message to request current RF configuration
API_MESSAGE_CHECK_GAIN = '{"message":"rf"}'

pp = pprint.PrettyPrinter(indent=4)

async def amarisoft_api_request(target, msg):
    uri = "ws://" + target
    print("Connecting to API URI:", uri)

    async with websockets.connect(uri, origin="Test") as websocket:
        # Wait for initial ready message
        ready = await websocket.recv()
        # Send request
        await websocket.send(msg)
        # Receive response
        rsp = await websocket.recv()
        return json.loads(rsp)

def main():
    print("Amarisoft check gain")
    print("Starting request to Amarisoft Callbox")
    now = datetime.now()

    requests_sent = 0
    response = None

    while response is None:
        try:
            response = asyncio.run(amarisoft_api_request(TARGET_ENB, API_MESSAGE_CHECK_GAIN))
            requests_sent += 1
            print(f"- Request {requests_sent} sent")
        except Exception as e:
            print(f"EXCEPTION: {e}. Retrying...")

    print("DONE! Current RF configuration:")
    pp.pprint(response)

    # Optional: print just the gains
    if "tx_gain" in response:
        print(f"\nTX Gain: {response['tx_gain']}")
    if "rx_gain" in response:
        print(f"RX Gain: {response['rx_gain']}")

if __name__ == "__main__":
    main()
