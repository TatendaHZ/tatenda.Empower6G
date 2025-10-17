import asyncio
import websockets
import json
import sys
from datetime import datetime
import pprint
import os

# Local configuration
LOCAL = True

if LOCAL:
    TARGET_ENB = "192.168.88.53:9001"   # Update with your gNB IP
    TARGET_MME = "192.168.88.53:9000"
else:
    TARGET_ENB = str(os.environ.get("TARGET_ENB"))
    TARGET_MME = str(os.environ.get("TARGET_MME"))

# Define gain presets (values in dB)
GAIN_PRESETS = {
    "low": {
        "tx_gain": [60.0, 60.0],
        "rx_gain": [30.0]
    },
    "medium": {
        "tx_gain": [75.0, 75.0],
        "rx_gain": [45.0]
    },
    "high": {
        "tx_gain": [85.0, 85.0],
        "rx_gain": [55.0]
    },
    "max": {
        "tx_gain": [89.75, 89.75],
        "rx_gain": [60.0]
    }
}

pp = pprint.PrettyPrinter(indent=4)

async def amarisoft_api_request(target, msg):
    uri = "ws://" + target
    print(f"Requesting to API URI: {uri}")

    async with websockets.connect(uri, origin="Test") as websocket:
        await websocket.recv()  # initial ready message
        await websocket.send(msg)
        rsp = await websocket.recv()
        return json.loads(rsp)

def build_gain_message(level):
    if level not in GAIN_PRESETS:
        raise ValueError(f"Invalid gain level '{level}'. Valid options are: {list(GAIN_PRESETS.keys())}")
    gain_conf = GAIN_PRESETS[level]
    message = {"message": "rf"}
    message.update(gain_conf)
    return json.dumps(message)

def main():
    if len(sys.argv) < 2:
        print("Usage: python change_gain.py [low|medium|high|max]")
        sys.exit(1)

    level = sys.argv[1].lower()
    print(f"🔸 Changing Amarisoft gain to: {level.upper()}")

    api_message = build_gain_message(level)
    print(f"📡 Sending message: {api_message}")

    try:
        json_rsp = asyncio.run(amarisoft_api_request(TARGET_ENB, api_message))
        print("\n✅ Gain successfully updated. Current RF configuration:")
        pp.pprint(json_rsp)
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")

if __name__ == "__main__":
    main()
