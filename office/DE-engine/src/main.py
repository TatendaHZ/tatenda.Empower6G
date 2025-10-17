from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List
import uuid
import asyncio

# Import anomaly detection
from src.algorithms.anomaly_detection import AnomalyDetection, read_metrics

app = FastAPI(title="Decision Engine API", version="1.0.0")

# -------------------------------
# Models
# -------------------------------
class Execution(BaseModel):
    id: str
    algorithm: str
    status: str

class User(BaseModel):
    id: str
    name: str


# -------------------------------
# Global storage for anomalies
# -------------------------------
latest_anomalies = {"status": "no anomalies yet"}


# -------------------------------
# Background Task for Anomaly Detection
# -------------------------------
@app.on_event("startup")
async def start_background_tasks():
    asyncio.create_task(anomaly_detection_loop())

async def anomaly_detection_loop():
    detector = AnomalyDetection()
    while True:
        metrics = read_metrics()
        if metrics:
            try:
                anomalies = detector.run(metrics)
                globals()["latest_anomalies"] = anomalies
            except Exception as e:
                print(f"Error running anomaly detection: {e}")
        await asyncio.sleep(2)  # wait 2 seconds before next run


@app.get("/api/v1/decision_engine/anomalies", tags=["Anomaly Detection"])
async def get_anomalies():
    """Expose latest anomaly detection result"""
    return latest_anomalies


# -------------------------------
# Algorithm Execution
# -------------------------------
@app.get("/api/v1/decision_engine/history", tags=["Algorithm Execution"])
def get_history():
    return {"message": "Get all executions"}

@app.get("/api/v1/decision_engine/executions", tags=["Algorithm Execution"])
def get_executions():
    return {"message": "Get active executions"}

@app.post("/api/v1/decision_engine/execution", tags=["Algorithm Execution"])
def start_execution():
    return {"message": "Start execution"}

@app.get("/api/v1/decision_engine/execution/{uuid}", tags=["Algorithm Execution"])
def get_execution(uuid: str = Path(...)):
    return {"message": f"Get execution {uuid}"}

@app.delete("/api/v1/decision_engine/execution/{uuid}", tags=["Algorithm Execution"])
def delete_execution(uuid: str = Path(...)):
    return {"message": f"Delete execution {uuid}"}

@app.get("/api/v1/decision_engine/statistics", tags=["Algorithm Execution"])
def get_statistics():
    return {"message": "Get statistics"}

@app.get("/api/v1/decision_engine/logs/{uuid}", tags=["Algorithm Execution"])
def get_logs(uuid: str = Path(...)):
    return {"message": f"Get logs {uuid}"}


# -------------------------------
# Execution Engines
# -------------------------------
@app.get("/api/v1/decision_engine/engines", tags=["Execution Engines"])
def get_engines():
    return {"message": "List engines"}

@app.get("/api/v1/decision_engine/engines/{uuid}", tags=["Execution Engines"])
def get_engine(uuid: str = Path(...)):
    return {"message": f"Get engine {uuid}"}


# -------------------------------
# User Management
# -------------------------------
@app.get("/api/v1/decision_engine/users", tags=["User Management"])
def get_users():
    return {"message": "List users"}

@app.post("/api/v1/decision_engine/users", tags=["User Management"])
def add_user(user: User):
    return {"message": f"Add user {user.name}"}

@app.get("/api/v1/decision_engine/users/{uuid}", tags=["User Management"])
def get_user(uuid: str = Path(...)):
    return {"message": f"Get user {uuid}"}

@app.delete("/api/v1/decision_engine/users/{uuid}", tags=["User Management"])
def delete_user(uuid: str = Path(...)):
    return {"message": f"Delete user {uuid}"}
