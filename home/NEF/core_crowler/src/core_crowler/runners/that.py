import subprocess
import time
import re
import json
import os
from pymongo import MongoClient
import logging

def setup_logger(log_level=logging.INFO, logger_name="malogga"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger

logger = setup_logger(logger_name="o5gs_middleware")

class O5GSMiddleware:
    def __init__(self, mongo_uri="mongodb://10.98.77.174:27017", db_name="amf_logs", collection_name="location_info"):
        try:
            self.mongo_client = MongoClient(mongo_uri)
            self.mongo_db = self.mongo_client[db_name]
            self.mongo_collection = self.mongo_db[collection_name]
            logger.info("[MONGODB] Connected to MongoDB")
        except Exception as e:
            logger.error(f"[MONGODB] Failed to connect: {e}")
            self.mongo_collection = None

    def write_location_info(self, event):
        if self.mongo_collection is not None:
            refined_event = {
                "_id": event["_id"],
                "cellId": event["amf_info"]["ueLocation"]["nrLocation"]["ncgi"]["nrCellId"],
                "trackingAreaId": event["amf_info"]["ueLocation"]["nrLocation"]["tai"]["tac"],
                "plmnId": event["amf_info"]["guami"]["plmnId"],
                "routingAreaId": None,
                "enodeBId": None,
                "twanId": None,
                "UELocationTimestamp": event["amf_info"]["ueLocation"]["nrLocation"]["ueLocationTimestamp"]
            }
            try:
                self.mongo_collection.replace_one({"_id": event["_id"]}, refined_event, upsert=True)
                logger.info(f"[MONGODB] Stored location for IMSI: {event['_id']}")
                logger.info(json.dumps(refined_event, indent=4))
            except Exception as e:
                logger.error(f"[MONGODB] Failed to insert location: {e}")

logger = setup_logger(logger_name="amf_log_parser")
KEYS = ["supi", "pei", "ueLocation", "ueTimeZone"]

class LogParser:
    def __init__(self, mongo_uri="mongodb://10.98.77.174:27017", db_name="amf_logs", collection_name="ue_events"):
        self.event_history = []
        try:
            self.mongo_client = MongoClient(mongo_uri)
            self.mongo_db = self.mongo_client[db_name]
            self.mongo_collection = self.mongo_db[collection_name]
            logger.info("[MONGODB] Connected to MongoDB")
        except Exception as e:
            logger.error(f"[MONGODB] Failed to connect: {e}")
            self.mongo_collection = None
        self.json_pattern = re.compile(r'(\{.*\})', re.DOTALL)
        self.mdlw = O5GSMiddleware(mongo_uri=mongo_uri, db_name=db_name)

    def process_line(self, line):
        line = line.strip()
        match = self.json_pattern.search(line)
        if match:
            json_str = match.group(1)
            try:
                json_data = json.loads(json_str)
                missing_keys = [key for key in KEYS if key not in json_data]
                if missing_keys:
                    return self.handle_registration_json(json_data)
            except json.JSONDecodeError:
                pass
        return

    def handle_registration_json(self, json_data):
        supi = json_data.get("supi")
        if not supi:
            return
        imsi = supi.replace("imsi-", "")
        event = {"_id": imsi, "amf_info": json_data}
        if self.mongo_collection is not None:
            try:
                self.mongo_collection.replace_one({"_id": imsi}, event, upsert=True)
                logger.info(f"[MONGODB] Stored registration for IMSI: {imsi}")
                logger.info(json.dumps(event, indent=4))
                self.mdlw.write_location_info(event)
            except Exception as e:
                logger.error(f"[MONGODB] Failed to insert registration: {e}")

MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASS = os.getenv("MONGO_PASS", "secret")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "amf_logs")
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

logger = setup_logger(logger_name="amf_log_parser")
parser = LogParser(mongo_uri=MONGO_URI, db_name=MONGO_DB_NAME, collection_name="ue_events")
logger = setup_logger(logger_name="amf_log_watcher_k8s")

class K8sLogFetcher:
    def __init__(self, pod_name: str, container_name: str = None, namespace: str = "default", poll_interval: int = 2):
        self.pod_name = pod_name
        self.container_name = container_name
        self.namespace = namespace
        self.poll_interval = poll_interval
        self.last_logs = []

    def clean_ansi_codes(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def fetch_logs(self):
        cmd = ["kubectl", "logs", self.pod_name, "-n", self.namespace, "--tail=100"]
        if self.container_name:
            cmd += ["-c", self.container_name]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            lines = [self.clean_ansi_codes(line.strip()) for line in result.stdout.splitlines()]
        except Exception as e:
            logger.error(f"[ERROR] Failed to fetch logs: {e}")
            return []
        self.last_logs = lines
        return lines

    def run(self, handler_fn):
        logger.info(f"[INFO] Watching pod '{self.pod_name}' logs every {self.poll_interval}s...")
        try:
            while True:
                logs = self.fetch_logs()
                if logs:
                    handler_fn(logs)
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            logger.info("\n[INTERRUPT] Displaying final event history...")
            handler_fn(self.last_logs)

def handle_logs(logs):
    for log in logs:
        logger.info(f"[LOG] {log}")

if __name__ == "__main__":
    container_name = os.getenv("TARGET_CONTAINER_NAME", "amf")
    namespace = os.getenv("TARGET_NAMESPACE", "open5gs")
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace, "--no-headers", "-o", "custom-columns=:metadata.name"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        all_pods = result.stdout.splitlines()
        pod_name = next((p for p in all_pods if p.startswith("amf-depl")), None)
        if not pod_name:
            raise RuntimeError("No AMF pod found with prefix 'amf-depl'")
        logger.info(f"[INFO] Using AMF pod: {pod_name}")
        fetcher = K8sLogFetcher(pod_name=pod_name, container_name=container_name, namespace=namespace, poll_interval=2)
        fetcher.run(handle_logs)
    except Exception as e:
        logger.error(f"[ERROR] Failed to resolve AMF pod: {e}")
