#!/bin/bash

echo "Simulating service stop..."
ssh pi-host "sudo systemctl stop my-demo-service"

echo "Triggering remediation through controller..."
curl -X POST http://localhost:8000/remediate \
  -H "Content-Type: application/json" \
  -d '{"host":"pi-host","service":"my-demo-service"}'

echo "Checking service status..."
ssh pi-host "systemctl is-active my-demo-service"
