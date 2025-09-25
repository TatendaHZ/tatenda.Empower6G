import subprocess
import time
import json
import signal
import sys
from pymongo import MongoClient

# Kubernetes settings
K8S_NAMESPACE = "open5gs"
MONGO_SERVICE = "mongodb-svc"
LOCAL_PORT = 27017
REMOTE_PORT = 27017

def convert_ambr_to_value_unit(ambr_str):
    """Convert string-based AMBR (e.g., '5 Mbps') to {value, unit} format."""
    try:
        value, unit = ambr_str.split()
        value = float(value)
        if unit == "Gbps":
            value *= 1000  # Convert Gbps to Mbps
        return {"value": int(value), "unit": 3}  # Unit 3 for Mbps
    except Exception as e:
        print(f"Error converting AMBR '{ambr_str}': {e}")
        return None

# Read APN configuration from JSON file
try:
    with open("apn_config.json", "r") as file:
        apn_config = json.load(file)
    apn_template = apn_config.get("apn_template", {})
except Exception as e:
    print(f"Error reading apn_config.json: {e}")
    sys.exit(1)

# Start kubectl port-forward
print(f"Starting port-forward to {MONGO_SERVICE} in namespace {K8S_NAMESPACE}...")
pf_process = subprocess.Popen(
    ["kubectl", "port-forward", f"svc/{MONGO_SERVICE}", f"{LOCAL_PORT}:{REMOTE_PORT}", "-n", K8S_NAMESPACE],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Give port-forward a moment to establish
time.sleep(2)

try:
    # Connect to MongoDB via the forwarded port
    client = MongoClient("127.0.0.1", LOCAL_PORT)
    db = client["open5gs"]
    subscribers_collection = db["subscribers"]

    # Prepare the subscribed_apns list from apn_template
    subscribed_apns = [
        {"apn": apn_name, **apn_details} for apn_name, apn_details in apn_template.items()
    ]

    # Update all documents in the subscribers collection
    for subscriber in subscribers_collection.find():
        updated_slices = []
        for slice in subscriber.get("slice", []):
            updated_sessions = []
            for session in slice.get("session", []):
                apn_name = session.get("name")
                if apn_name in apn_template:
                    # Update session AMBR based on apn_config.json
                    ambr_config = apn_template[apn_name]["ambr"]
                    uplink = convert_ambr_to_value_unit(ambr_config["uplink"])
                    downlink = convert_ambr_to_value_unit(ambr_config["downlink"])
                    if uplink and downlink:
                        session["ambr"] = {"uplink": uplink, "downlink": downlink}
                updated_sessions.append(session)
            slice["session"] = updated_sessions
            updated_slices.append(slice)

        # Update the subscriber document
        result = subscribers_collection.update_one(
            {"_id": subscriber["_id"]},
            {
                "$set": {
                    "subscribed_apns": subscribed_apns,
                    "slice": updated_slices
                }
            }
        )
        if result.modified_count > 0:
            print(f"Updated subscriber with IMSI {subscriber['imsi']}")

    print("New subscribed_apns configuration:")
    print(json.dumps(subscribed_apns, indent=2))
    print("Note: slice.session.ambr fields have been updated to match apn_config.json.")

except Exception as e:
    print(f"Error updating MongoDB: {e}")

finally:
    print("Stopping port-forward...")
    pf_process.send_signal(signal.SIGINT)  # Gracefully stop port-forward
    pf_process.wait()
    sys.exit(0)
