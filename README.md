# Edge Fleet Manager — Autonomous Self-Healing Agent

A lightweight agent-based system that monitors Raspberry Pi services, detects failures, and automatically remediates them using SSH or Ansible. Built as part of the Kaggle Agents Intensive Capstone Project.

---

## Features

- Heartbeat-based health monitoring
- Detects service crashes
- Monitors disk usage
- Automatic or manual remediation
- SSH-based service restart
- Optional Ansible integration
- Audit log of all remediation actions
- Works on any Linux host (not just Raspberry Pi)

---

## Architecture

+-----------------------+ Heartbeat +---------------------------+
| Edge Agent | ------------------> | Controller Agent |
| (Raspberry Pi) | | (FastAPI Orchestrator) |
| - Check service | | - Show agent statuses |
| - Check disk | | - Trigger remediation |
+-----------------------+ <------ SSH ------- +---------------------------+

local service restart via systemd

---

## Quickstart

### 1. Start the Controller
```bash
cd controller
uvicorn app.main:app --port 8000```
2. Start the Agent
```cd agent
python agent.py```
3. View Agent Status
```curl http://localhost:8000/agents```
4. Simulate Failure
```sudo systemctl stop my-demo-service```
5. Trigger Remediation
```curl -X POST http://localhost:8000/remediate \
  -H "Content-Type: application/json" \
  -d '{"host":"pi-host","service":"my-demo-service"}'```

Project Structure
```agent/
  agent.py
  requirements.txt

controller/
  app/
    main.py
  requirements.txt

ansible/
  restart_service.yml

demo/
  demo_script.sh```

License

MIT / CC-BY-4.0 depending on your preference.
```
---
