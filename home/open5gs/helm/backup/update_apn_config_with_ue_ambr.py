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

# Read APN configuration from JSON file
try:
    with open("apn_config.json", "r") as file:
        apn_config = json.load(file)
    apn_template = apn_config.get("apn_template", {})
    ue_ambr = apn_config.get("ue_ambr", {})
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
        {
            "apn": apn_name,
            "5qi": apn_details["5qi"],
            "qci": apn_details["qci"],
            "priority_level": apn_details["priority_level"],
            "ambr": apn_details["ambr"]
        }
        for apn_name, apn_details in apn_template.items()
    ]

    # Update all documents in the subscribers collection
    for subscriber in subscribers_collection.find():
        print(f"\nBefore update for IMSI {subscriber['imsi']}:")
        print("subscribed_apns:", json.dumps(subscriber.get("subscribed_apns", []), indent=2))
        print("slice.session.ambr:")
        for slice in subscriber.get("slice", []):
            for session in slice.get("session", []):
                print(f"  {session['name']}: {json.dumps(session['ambr'], indent=2)}")
        print("ue_ambr:", json.dumps(subscriber.get("ambr", {}), indent=2))

        updated_slices = []
        for slice in subscriber.get("slice", []):
            updated_sessions = []
            for session in slice.get("session", []):
                apn_name = session.get("name")
                if apn_name in apn_template:
                    # Update session AMBR, QoS, and type based on apn_config.json
                    session["ambr"] = apn_template[apn_name]["slice_ambr"]
                    session["qos"] = apn_template[apn_name]["qos"]
                    session["type"] = apn_template[apn_name]["type"]
                updated_sessions.append(session)
            slice["session"] = updated_sessions
            updated_slices.append(slice)

        # Update the subscriber document
        result = subscribers_collection.update_one(
            {"_id": subscriber["_id"]},
            {
                "$set": {
                    "subscribed_apns": subscribed_apns,
                    "slice": updated_slices,
                    "ambr": {
                        "downlink": {
                            "value": ue_ambr["downlink"]["value"],
                            "unit": ue_ambr["downlink"]["unit"]
                        },
                        "uplink": {
                            "value": ue_ambr["uplink"]["value"],
                            "unit": ue_ambr["uplink"]["unit"]
                        }
                    }
                }
            }
        )
        if result.modified_count > 0:
            print(f"Updated subscriber with IMSI {subscriber['imsi']}")
            updated_subscriber = subscribers_collection.find_one({"_id": subscriber["_id"]})
            print(f"After update for IMSI {subscriber['imsi']}:")
            print("subscribed_apns:", json.dumps(updated_subscriber.get("subscribed_apns", []), indent=2))
            print("slice.session.ambr:")
            for slice in updated_subscriber.get("slice", []):
                for session in slice.get("session", []):
                    print(f"  {session['name']}: {json.dumps(session['ambr'], indent=2)}")
            print("ue_ambr:", json.dumps(updated_subscriber.get("ambr", {}), indent=2))

    print("\nNew subscribed_apns configuration:")
    print(json.dumps(subscribed_apns, indent=2))
    print("New ue_ambr configuration:")
    print(json.dumps(ue_ambr, indent=2))
    print("Note: slice.session.ambr and ue_ambr fields have been updated to match apn_config.json, with unit: 3 for Mbps and unit: 2 for Kbps.")

except Exception as e:
    print(f"Error updating MongoDB: {e}")

finally:
    print("Stopping port-forward...")
    pf_process.send_signal(signal.SIGINT)  # Gracefully stop port-forward
    pf_process.wait()
    sys.exit(0)
