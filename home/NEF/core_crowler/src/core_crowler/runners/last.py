import subprocess
import time
import re
import json
import os
from pymongo import MongoClient, errors
import logging

# -------------------------------
# Logger Setup
# -------------------------------
def setup_logger(log_level=logging.INFO, logger_name="amf_logger"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    if not logger.hasHandlers():
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

logger = setup_logger()

# -------------------------------
# MongoDB Middleware
# -------------------------------
class MongoMiddleware:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=5000)
            self.db = self.client[self.db_name]
            # Test connection
            self.client.admin.command('ping')
            logger.info(f"[MONGO] Connected to {self.db_name}")
        except errors.ServerSelectionTimeoutError as e:
            logger.error(f"[MONGO] Connection failed: {e}")
            self.client = None

    def get_collection(self, collection_name):
        if self.db:
            return self.db[collection_name]
        else:
            logger.error("[MONGO] No DB connection")
            return None

    def upsert_event(self, collection_name, event_id, data):
        coll = self.get_collection(collection_name)
        if coll:
            try:
                coll.replace_one({"_id": event_id}, data, upsert=True)
                logger.info(f"[MONGO] Stored event {_short_id(event_id)} in {collection_name}")
            except Exception as e:
                logger.error(f"[MONGO] Failed to write event: {e}")

def _short_id(event_id):
    return str(event_id)[:8]

# -------------------------------
# Log Parser
# -------------------------------
KEYS = ["supi", "pei", "ueLocation", "ueTimeZone"]

class AMFLogParser:
    def __init__(self, mongo_middleware, collection_name="ue_events"):
        self.mongo = mongo_middleware
        self.collection_name = collection_name
        self.json_regex = re.compile(r'(\{.*\})', re.DOTALL)

    def process_line(self, line):
        line = line.strip()
        match = self.json_regex.search(line)
        if not match:
            return

        try:
            data = json.loads(match.group(1))
            supi = data.get("supi")
            if not supi:
                return
            imsi = supi.replace("imsi-", "")
            event = {"_id": imsi, "amf_info": data}

            # Write to main collection
            self.mongo.upsert_event(self.collection_name, imsi, event)

            # Optionally refine and store location info
            loc = self._extract_location(event)
            if loc:
                self.mongo.upsert_event("location_info", imsi, loc)

        except json.JSONDecodeError:
            pass

    def _extract_location(self, event):
        try:
            info = event["amf_info"]
            loc_event = {
                "_id": event["_id"],
                "cellId": info["ueLocation"]["nrLocation"]["ncgi"]["nrCellId"],
                "trackingAreaId": info["ueLocation"]["nrLocation"]["tai"]["tac"],
                "plmnId": info["guami"]["plmnId"],
                "routingAreaId": None,
                "enodeBId": None,
                "twanId": None,
                "UELocationTimestamp": info["ueLocation"]["nrLocation"]["ueLocationTimestamp"]
            }
            return loc_event
        except KeyError:
            return None

# -------------------------------
# Kubernetes Log Fetcher
# -------------------------------
class K8sLogWatcher:
    def __init__(self, pod_name, container_name=None, namespace="default", interval=2):
        self.pod_name = pod_name
        self.container_name = container_name
        self.namespace = namespace
        self.interval = interval
        self.last_logs = []

    def clean_ansi(self, text):
        return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', text)

    def fetch_logs(self):
        cmd = ["kubectl", "logs", self.pod_name, "-n", self.namespace, "--tail=100"]
        if self.container_name:
            cmd += ["-c", self.container_name]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            lines = [self.clean_ansi(l.strip()) for l in result.stdout.splitlines()]
            self.last_logs = lines
            return lines
        except Exception as e:
            logger.error(f"[K8S] Failed to fetch logs: {e}")
            return []

    def watch(self, parser):
        logger.info(f"[K8S] Watching pod {self.pod_name} logs every {self.interval}s")
        try:
            while True:
                logs = self.fetch_logs()
                for line in logs:
                    parser.process_line(line)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logger.info("[K8S] Stopped watching logs.")

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://10.98.77.174:27017")
    MONGO_DB = os.getenv("MONGO_DB_NAME", "amf_logs")
    POD_NAMESPACE = os.getenv("TARGET_NAMESPACE", "open5gs")
    POD_CONTAINER = os.getenv("TARGET_CONTAINER_NAME", "amf")

    # Find AMF pod dynamically
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", POD_NAMESPACE, "--no-headers", "-o", "custom-columns=:metadata.name"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        pods = result.stdout.splitlines()
        pod_name = next((p for p in pods if p.startswith("amf-depl")), None)
        if not pod_name:
            raise RuntimeError("No AMF pod found")
        logger.info(f"[INFO] Using pod: {pod_name}")

        mongo = MongoMiddleware(MONGO_URI, MONGO_DB)
        parser = AMFLogParser(mongo)
        watcher = K8sLogWatcher(pod_name, container_name=POD_CONTAINER, namespace=POD_NAMESPACE)
        watcher.watch(parser)

    except Exception as e:
        logger.error(f"[ERROR] Main failed: {e}")
