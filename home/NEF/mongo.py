import subprocess
import time
from pymongo import MongoClient
import logging
import signal
import sys

# Kubernetes settings
K8S_NAMESPACE = "open5gs"
MONGO_SERVICE = "mongodb-svc"
LOCAL_PORT = 27017
REMOTE_PORT = 27017

# MongoDB settings
DB_NAME = "amf_logs"
COLLECTIONS = ["ue_events", "location_info"]

# Setup logger
logger = logging.getLogger("mongo_test")
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(ch)

# Start kubectl port-forward
logger.info(f"Starting port-forward to {MONGO_SERVICE} in namespace {K8S_NAMESPACE}...")
pf_process = subprocess.Popen(
    ["kubectl", "port-forward", f"svc/{MONGO_SERVICE}", f"{LOCAL_PORT}:{REMOTE_PORT}", "-n", K8S_NAMESPACE],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Give port-forward a moment to establish
time.sleep(2)

try:
    # Connect to MongoDB via forwarded port
    client = MongoClient("127.0.0.1", LOCAL_PORT)
    db = client[DB_NAME]
    logger.info(f"[MONGODB] Connected to 127.0.0.1:{LOCAL_PORT}, DB: {DB_NAME}")

    # Ensure collections exist and insert test documents
    for col_name in COLLECTIONS:
        collection = db[col_name]
        test_doc = {"_id": f"test_{col_name}", "msg": f"Collection {col_name} ready"}
        collection.replace_one({"_id": test_doc["_id"]}, test_doc, upsert=True)
        logger.info(f"[MONGODB] Test document inserted in {col_name}: {test_doc}")

except Exception as e:
    logger.error(f"[MONGODB] Connection failed: {e}")

finally:
    logger.info("Stopping port-forward...")
    pf_process.send_signal(signal.SIGINT)
    pf_process.wait()
    sys.exit(0)
