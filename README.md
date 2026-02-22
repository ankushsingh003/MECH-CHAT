# MECH-CHAT | Agentic Fleet Control Center

MECH-CHAT is a premium, full-stack agentic orchestration system designed for high-performance vehicle fleet management. It leverages a multi-agent architecture to monitor telemetry, diagnose failures, and coordinate maintenance workflows with zero manual intervention.

![MECH-CHAT Dashboard](dashboard/preview.png) *(Placeholder if you have a screenshot)*

## 🚀 Key Features

### 1. **Context-Aware Agent Orchestration**
The system uses a **Master Orchestrator** to coordinate specialized agents in a chained workflow:
- **Telemetry Analyst**: Monitors battery heat, tire integrity, motor RPM, and cooling levels.
- **Diagnosis Engine**: Predicts specific failures (e.g., gearbox slippage, sensor punctures) based on anomalous data.
- **Voice Interface (SAPI)**: Generates human-like alerts and engagement messages for drivers.
- **Scheduling Agent**: Dynamically books specialized service slots based on the detected issue.
- **Quality Monitor**: Collects post-service feedback to ensure resolution.
- **Manufacturing Insights**: Performs Root Cause Analysis (RCA) and maps fleet failures back to factory component batches.

### 2. **Premium Dashboard UI**
- **Glassmorphism Design**: A sleek, commercial-grade interface with deep blurs and vibrant neon accents.
- **Live Orchestration Feed**: Real-time log streaming showing agent interactions as they happen.
- **SAPI Voice Wave**: Interactive voice pulse animation during customer engagement.
- **Dynamic Fleet Health**: Real-time health scoring and telemetry visualization for hundreds of vehicles.

### 3. **Security & Compliance (UEBA)**
- Integrated **User and Entity Behavior Analytics (UEBA)** monitor.
- Real-time security audits for every agent action.
- Automatic flagging of unauthorized service requests or anomalous system triggers.

### 4. **Scalable Architecture**
- **Deadlock-Free Logging**: High-performance in-memory logging system optimized for single-threaded Python environments.
- **Multithreaded Backend**: Asynchronous task execution allows the UI to stay responsive during complex agent workflows.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask, Flask-CORS
- **Frontend**: TypeScript, Vite, Vanilla CSS (Modern CSS3)
- **Architecture**: Multi-Agent System (MAS), RESTful API
- **Data**: Synthetic Telemetry Generator

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js & npm

### 1. Clone the Repository
```bash
git clone https://github.com/ankushs003/MECH-CHAT.git
cd MECH-CHAT
```

### 2. Setup Backend
```bash
# Install dependencies
pip install flask flask-cors requests

# Generate synthetic vehicle data
python data/generate_data.py

# Start the Mock Server
# Note: Use PYTHONPATH="." to ensure agent imports resolve
$env:PYTHONPATH="."; python api/mock_server.py
```

### 3. Setup Frontend
```bash
cd dashboard
npm install
npm run dev
```
The dashboard will be available at `http://localhost:3000`.

---

## 📂 Project Structure

- `agents/`: Logic for the various specialized agents.
- `api/`: Flask server implementation and API routes.
- `dashboard/`: Vite-based TypeScript frontend.
- `data/`: Synthetic data generation logic and JSON store.
- `security/`: UEBA monitor and audit systems.
- `sapi/`: Bridge for the SAPI voice interface.

---

## 🛡️ Security Audit
Every orchestration task is audited by the **UEBA Monitor**. You can view live system approvals and flags in the "Security Audit" panel on the dashboard.

---

## 📄 License
This project is for demonstration purposes. All rights reserved.
