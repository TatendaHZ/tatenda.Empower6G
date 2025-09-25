from fastapi import FastAPI, Request
import logging

app = FastAPI(title="Open5GS NEF Facade")
logging.basicConfig(level=logging.INFO)

@app.post("/3gpp-as-session-with-qos/v1/sessions")
async def create_qod_session(request: Request):
    body = await request.json()
    logging.info(f"Received QoD session request: {body}")
    # TODO: Translate to Open5GS MongoDB / SMF call
    return {"status": "QoD session accepted", "sessionId": "dummy-session-1"}

@app.get("/3gpp-as-session-with-qos/v1/sessions/{session_id}")
async def get_qod_session(session_id: str):
    logging.info(f"Querying QoD session: {session_id}")
    # TODO: Lookup from MongoDB / SMF
    return {"status": "QoD session retrieved", "sessionId": session_id}

@app.post("/3gpp-monitoring-event/v1/subscriptions")
async def create_location_subscription(request: Request):
    body = await request.json()
    logging.info(f"Received Location subscription request: {body}")
    # TODO: Map to AMF UE location retrieval
    return {"status": "Location subscription accepted", "subscriptionId": "dummy-sub-1"}
