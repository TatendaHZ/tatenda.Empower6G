  
import os
import time
import re
from datetime import datetime, timedelta
import logging
from pymongo import MongoClient


logger = setup_logger(logger_name="o5gs_middleware")

class O5GSMiddleware():
    def __init__(self, mongo_uri="mongodb://localhost:27017", db_name="amf_logs", collection_name="location_info"):
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
                "plmnId": event["amf_info"]["guami"]["plmnId"], # TODO: Check if this is correct
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

KEYS = [
    "supi",
    "pei",
    "ueLocation",
    "ueTimeZone",
]

class LogParser:
    def __init__(self, mongo_uri="mongodb://localhost:27017", db_name="amf_logs", collection_name="ue_events"):
        self.event_history = []

        try:
            self.mongo_client = MongoClient(mongo_uri)
            self.mongo_db = self.mongo_client[db_name]
            self.mongo_collection = self.mongo_db[collection_name]
            logger.info("[MONGODB] Connected to MongoDB")
        except Exception as e:
            logger.error(f"[MONGODB] Failed to connect: {e}")
            self.mongo_collection = None

        # Regex to match a complete JSON object in a line
        self.json_pattern = re.compile(r'(\{.*\})', re.DOTALL)

        self.mdlw = O5GSMiddleware(mongo_uri=mongo_uri, db_name=db_name)

    def process_line(self, line):
        line = line.strip()

        # Attempt to extract JSON from the line
        match = self.json_pattern.search(line)
        if match:
            json_str = match.group(1)
            try:
                json_data = json.loads(json_str)

                # Check if all required keys are present
                missing_keys = [key for key in KEYS if key not in json_data]
                if missing_keys:
                    return    
                self.handle_registration_json(json_data)
            except json.JSONDecodeError:
                pass
            return

    def handle_registration_json(self, json_data):
        supi = json_data.get("supi")
        if not supi:
            return

        imsi = supi.replace("imsi-", "")

        event = {
            "_id": imsi,
            "amf_info": json_data
        }

        #self.event_history.append(event)

        if self.mongo_collection is not None:
            try:
                self.mongo_collection.replace_one({"_id": imsi}, event, upsert=True)
                logger.info(f"[MONGODB] Stored registration for IMSI: {imsi}")
                logger.info(json.dumps(event, indent=4))
                self.mdlw.write_location_info(event)
            except Exception as e:
                logger.error(f"[MONGODB] Failed to insert registration: {e}")

def setup_logger(log_level=logging.INFO, logger_name="malogga"):
    """
    Sets up a logger to log messages to the console only.

    Args:
        log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
        logger_name (str): The name of the logger.

    Returns:
        logger (logging.Logger): Configured logger object.
    """
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Avoid adding handlers multiple times
    if not logger.hasHandlers():
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Define log format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        # Add handler to the logger
        logger.addHandler(console_handler)

    return logger
try:
    import docker
except ImportError:
    docker = None

import subprocess

logger = setup_logger(logger_name="amf_log_watcher")

class DockerLogFetcher:
    def __init__(self, container_name: str, poll_interval: int = 2):
        self.container_name = container_name
        self.poll_interval = poll_interval
        self.last_fetch_time = datetime.now()
        self.use_sdk = True

        if docker:
            try:
                self.client = docker.from_env()
                self.container = self.client.containers.get(container_name)
                self.use_sdk = True
                logger.info("[INFO] Docker SDK initialized.")
            except Exception as e:
                logger.warning(f"[WARN] Docker SDK failed: {e}. Falling back to CLI.")
        else:
            logger.warning("[WARN] Docker SDK not available. Falling back to CLI.")

    def clean_ansi_codes(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def parse_timestamp(self, line):
        match = re.match(r'(\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3}):', line)
        if not match:
            return None
        ts_str = match.group(1)
        full_ts_str = f"{datetime.now().year}/{ts_str}"
        try:
            return datetime.strptime(full_ts_str, "%Y/%m/%d %H:%M:%S.%f")
        except:
            return None

    def fetch_logs_sdk(self):
        logs = self.container.logs(since=int(self.last_fetch_time.timestamp()), stdout=True, stderr=True)
        lines = logs.decode("utf-8").splitlines()
        return lines

    def fetch_logs_cli(self):
        cmd = [
            "docker", "logs", self.container_name,
            "--since", self.last_fetch_time.isoformat()
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.splitlines()

    def fetch_logs(self):
        now = datetime.now()
        try:
            lines = self.fetch_logs_sdk() if self.use_sdk else self.fetch_logs_cli()
        except Exception as e:
            logger.error(f"[ERROR] Failed to fetch logs: {e}")
            return []

        logs = []
        for line in lines:
            line = self.clean_ansi_codes(line.strip())
            ts = self.parse_timestamp(line)
            if ts:
                logs.append((ts, line))
            elif "ueLocation" in line and logs:
                logs[-1] = (logs[-1][0], logs[-1][1] + " " + line)

        self.last_fetch_time = now
        return [l for _, l in logs]

    def run(self, handler_fn):
        logger.info(f"[INFO] Watching container '{self.container_name}' logs every {self.poll_interval}s...")
        while True:
            logs = self.fetch_logs()
            if logs:
                handler_fn(logs)
            time.sleep(self.poll_interval)

# -----------------------------
def handle_logs(logs):
    for log in logs:
        logger.info(f"[LOG] {log}")

if __name__ == "__main__":
    container_name = os.getenv("TARGET_CONTAINER_NAME", "amf")
    fetcher = DockerLogFetcher(container_name=container_name, poll_interval=2)
    fetcher.run(handle_logs)
# Need changes
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASS = os.getenv("MONGO_PASS", "secret")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "amf_logs")

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

# Logger setup
logger = setup_logger(logger_name="amf_log_parser")

# Parser and simulator setup
parser = LogParser(
    mongo_uri=MONGO_URI,
    db_name=MONGO_DB_NAME,
    collection_name="ue_events"
)

def handle_logs(logs):
    for log in logs:
        parser.process_line(log)

if __name__ == "__main__":
    simulator = DockerLogFetcher(
        container_name="amf",
        poll_interval=2
    )
    try:
        simulator.run(handle_logs)
    except KeyboardInterrupt:
        logger.info("\n[INTERRUPT] Displaying final event history...")
