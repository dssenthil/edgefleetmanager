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

# ✅ 5. YouTube Demo Script (60–90 seconds)

### **Total Length: ~75 seconds**

---

### **[0:00–0:05] — Intro**
“Welcome to my Kaggle Agents Intensive Capstone project: the Edge Fleet Manager.”

---

### **[0:05–0:15] — Problem**
“Managing multiple Raspberry Pis manually is slow and error-prone. Services crash, logs fill disks, and you have to SSH into each device to fix them.”

---

### **[0:15–0:25] — Solution**
“So I built a lightweight self-healing agent system. An agent runs on each Pi and sends health data to a FastAPI controller, which can automatically restart failing services.”

---

### **[0:25–0:40] — Architecture Image**
“Here’s the architecture: the Edge Agent checks service and disk health, sends heartbeats to the controller, and the controller triggers remediation using SSH or Ansible.”

(Show the architecture image)

---

### **[0:40–1:00] — Live Demo**
“Here’s the demo. On the right, I stop a service manually. The controller detects it as inactive. I trigger remediation, and the controller restarts the service successfully.”

(Show terminal windows, `/agents`, and `actions.log`)

---

### **[1:00–1:15] — Wrap-Up**
“This small system reduces my home-lab maintenance by 1–2 hours weekly. With more time, I’d add Home Assistant notifications, container restarts, and Prometheus metrics.”

---

### **[1:15] — End**
“Thanks for watching. Full code is in the GitHub repo linked below.”

---

# 🎯 All deliverables complete.

If you'd like, I can now:

- Generate a **second style** architecture diagram (colored, enterprise look)  
- Create a **shorter version** of the writeup  
- Polish your GitHub repo description  
- Generate a **credits / outro** screen for your YouTube video  

Just tell me!```

