import time
import socket
import requests
import subprocess
import os
import json

CONTROLLER = os.environ.get("CONTROLLER_URL", "http://localhost:8000")
AGENT_ID = os.environ.get("AGENT_ID", socket.gethostname())
SERVICE = os.environ.get("SERVICE_NAME", "my-demo-service")

def check_service(service):
    try:
        r = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True,
            timeout=5
        )
        return r.stdout.strip()
    except:
        return "unknown"

def get_disk_usage():
    stat = os.statvfs("/")
    used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
    total = stat.f_blocks * stat.f_frsize
    if total == 0:
        return 0
    return round((used / total) * 100, 2)

def send_heartbeat():
    payload = {
        "agent_id": AGENT_ID,
        "host": socket.gethostname(),
        "cpu": 0.0,
        "disk_percent": get_disk_usage(),
        "services": {SERVICE: check_service(SERVICE)}
    }

    try:
        r = requests.post(f"{CONTROLLER}/heartbeat", json=payload, timeout=5)
        print("Heartbeat sent:", r.status_code)
    except Exception as e:
        print("Failed to send heartbeat:", e)

if __name__ == "__main__":
    while True:
        send_heartbeat()
        time.sleep(30)
