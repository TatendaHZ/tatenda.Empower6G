import subprocess
import time
from pymongo import MongoClient
import json
import signal
import sys

# Kubernetes settings
K8S_NAMESPACE = "open5gs"
MONGO_SERVICE = "mongodb-svc"
LOCAL_PORT = 27017
REMOTE_PORT = 27017

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

    # List collections
    collections = db.list_collection_names()
    print(f"Found collections: {collections}\n")

    # Loop through and dump data
    for collection_name in collections:
        print(f"=== Collection: {collection_name} ===")
        documents = list(db[collection_name].find({}))
        print(json.dumps(documents, indent=2, default=str))
        print("\n")

except Exception as e:
    print("Error:", e)

finally:
    print("Stopping port-forward...")
    pf_process.send_signal(signal.SIGINT)  # Gracefully stop port-forward
    pf_process.wait()
    sys.exit(0)

