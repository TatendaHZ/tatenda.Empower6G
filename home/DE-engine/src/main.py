from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(
    title="Decision Engine API",
    description="Decision Engine - Access Interface REST API",
    version="1.0.0"
)

executions = {}
engines = {"simple_rule_detection": {"uuid": "engine-1"}}
users = {}

# Models
class ExecutionRequest(BaseModel):
    execution_params: dict
    algorithm_module: str

# Algorithm Execution
@app.get("/api/v1/decision_engine/history")
def get_history():
    return list(executions.values())

@app.get("/api/v1/decision_engine/executions")
def get_executions():
    return executions

@app.post("/api/v1/decision_engine/execution")
def start_execution(req: ExecutionRequest):
    eid = str(uuid.uuid4())
    executions[eid] = {"id": eid, "params": req.execution_params, "algo": req.algorithm_module, "status": "running"}
    return executions[eid]

@app.get("/api/v1/decision_engine/execution/{uuid}")
def get_execution(uuid: str):
    return executions.get(uuid, {"error": "Not found"})

@app.delete("/api/v1/decision_engine/execution/{uuid}")
def delete_execution(uuid: str):
    return executions.pop(uuid, {"error": "Not found"})

# Execution Engines
@app.get("/api/v1/decision_engine/engines")
def get_engines():
    return engines

@app.get("/api/v1/decision_engine/engines/{uuid}")
def get_engine(uuid: str):
    return engines.get(uuid, {"error": "Not found"})

# User Management
@app.get("/api/v1/decision_engine/users")
def get_users():
    return users

@app.post("/api/v1/decision_engine/users")
def add_user(user: dict):
    uid = str(uuid.uuid4())
    users[uid] = user
    return {"uuid": uid, "user": user}
