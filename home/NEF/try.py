from pymongo import MongoClient
import logging
import json
import os
from getpass import getpass

# Setup logger
logger = logging.getLogger("mongo_test")
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(ch)

# Hardcoded MongoDB connection
MONGO_URI = "mongodb://10.98.77.174:27017"
DB_NAME = "amf_logs"
UE_COLLECTION = "ue_events"
LOC_COLLECTION = "location_info"

# Optional paths for JSON files
UE_FILE = "ue_events.json"
LOC_FILE = "location_info.json"

def connect_mongo(uri, username=None, password=None):
    try:
        if username and password:
            client = MongoClient(uri, username=username, password=password)
        else:
            client = MongoClient(uri)
        # Test connection
        client.admin.command('ping')
        return client
    except Exception as e:
        return e

# Try connecting without auth first
client = connect_mongo(MONGO_URI)
if isinstance(client, Exception):
    logger.warning(f"[MONGODB] Connection failed: {client}")
    logger.info("[MONGODB] DB may require authentication. Please enter credentials.")
    username = input("MongoDB username: ")
    password = getpass("MongoDB password: ")
    client = connect_mongo(MONGO_URI, username=username, password=password)
    if isinstance(client, Exception):
        logger.error(f"[MONGODB] Connection failed even with credentials: {client}")
        exit(1)

try:
    db = client[DB_NAME]

    # Create collections
    ue_col = db[UE_COLLECTION]
    loc_col = db[LOC_COLLECTION]

    logger.info(f"[MONGODB] Connected to {MONGO_URI}, DB: {DB_NAME}")
    logger.info(f"[MONGODB] Collections ready: {UE_COLLECTION}, {LOC_COLLECTION}")

    # Insert documents from JSON files if they exist
    if os.path.exists(UE_FILE):
        with open(UE_FILE) as f:
            ue_docs = json.load(f)
            if isinstance(ue_docs, list):
                ue_col.insert_many(ue_docs)
            else:
                ue_col.insert_one(ue_docs)
        logger.info(f"[MONGODB] Inserted documents from {UE_FILE} into {UE_COLLECTION}")

    if os.path.exists(LOC_FILE):
        with open(LOC_FILE) as f:
            loc_docs = json.load(f)
            if isinstance(loc_docs, list):
                loc_col.insert_many(loc_docs)
            else:
                loc_col.insert_one(loc_docs)
        logger.info(f"[MONGODB] Inserted documents from {LOC_FILE} into {LOC_COLLECTION}")

    # Optional: insert a test document
    test_doc = {"_id": "test123", "msg": "Mongo collections created!"}
    ue_col.replace_one({"_id": test_doc["_id"]}, test_doc, upsert=True)
    loc_col.replace_one({"_id": test_doc["_id"]}, test_doc, upsert=True)
    logger.info(f"[MONGODB] Test documents inserted into both collections")

except Exception as e:
    logger.error(f"[MONGODB] Error while working with DB: {e}")
