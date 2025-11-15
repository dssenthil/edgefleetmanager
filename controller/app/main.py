from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import json
import time
from pathlib import Path

app = FastAPI()

AGENTS = {}  # agent_id -> last heartbeat
LOGFILE = Path(__file__).resolve().parents[2] / "actions.log"

class Heartbeat(BaseModel):
    agent_id: str
    host: str
    cpu: float = 0.0
    disk_percent: float = 0.0
    services: dict = {}

@app.post("/heartbeat")
async def heartbeat(data: Heartbeat):
    AGENTS[data.agent_id] = {
        "host": data.host,
        "cpu": data.cpu,
        "disk": data.disk_percent,
        "services": data.services,
        "timestamp": time.time()
    }
    return {"ok": True}

@app.get("/agents")
async def get_agents():
    return AGENTS

class RemediationRequest(BaseModel):
    host: str
    service: str

def log_action(entry: dict):
    LOGFILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOGFILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

@app.post("/remediate")
async def remediate(request: RemediationRequest):
    cmd = ["ssh", request.host, "sudo", "systemctl", "restart", request.service]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        success = result.returncode == 0

        log_action({
            "timestamp": time.time(),
            "host": request.host,
            "service": request.service,
            "command": " ".join(cmd),
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": success
        })

        return {"success": success, "stdout": result.stdout, "stderr": result.stderr}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
