# MECH-CHAT | Agentic Fleet Control Center

MECH-CHAT is a premium, full-stack agentic orchestration system designed for high-performance vehicle fleet management. It leverages a multi-agent architecture to monitor telemetry, diagnose failures, and coordinate maintenance workflows with zero manual intervention.

![MECH-CHAT Dashboard](dashboard/preview.png) *(Placeholder if you have a screenshot)*

## 🏗️ System Architecture & Orchestration

MECH-CHAT operates on a strictly vertical agentic chain, ensuring security and compliance at every step.

```mermaid
flowchart TD
    %% Node Definitions
    UI["💻 PREMIUM DASHBOARD<br/>(Vite + TypeScript)"]
    MO{"⚙️ MASTER ORCHESTRATOR<br/>(Core Logic)"}
    
    AA["🔍 TELEMETRY ANALYST<br/>(Anomaly Detection)"]
    DA["🧠 DIAGNOSIS ENGINE<br/>(Failure Prediction)"]
    EA["🗣️ ENGAGEMENT AGENT<br/>(SAPI Interface)"]
    SA["📅 SCHEDULING AGENT<br/>(Service Coordination)"]
    FA["⭐ FEEDBACK AGENT<br/>(Quality Monitor)"]
    IA["🏭 MANUFACTURING RCA<br/>(Root Cause Analysis)"]

    Audit["🛡️ UEBA MONITOR<br/>(Security Audit)"]

    %% Flow/Connections
    UI ====>|Interactive Trigger| MO
    
    subgraph "The Orchestration Pipeline"
        direction TB
        MO --> AA
        AA --> DA
        DA --> EA
        EA --> SA
        SA --> FA
        FA --> IA
    end

    MO -.- Audit
    Audit -.- AA
    Audit -.- DA
    
    %% Styling
    classDef primary fill:#0a0f19,stroke:#00f2ff,stroke-width:2px,color:#fff;
    classDef agent fill:#111,stroke:#94a3b8,color:#f1f5f9;
    classDef security fill:#1a0505,stroke:#ff4d4d,color:#ff4d4d;
    classDef ui fill:#030508,stroke:#00f2ff,color:#fff;

    class UI ui;
    class MO primary;
    class AA,DA,EA,SA,FA,IA agent;
    class Audit security;

    %% Global Spacing
    linkStyle default stroke:#94a3b8,stroke-width:1px;
```

### 🚀 High-Level Workflow
1. **Detection**: Data Analysis Agent monitors Heat, Tires, RPM, and Coolant.
2. **Alert**: SAPI interface engages the driver with personalized voice alerts.
3. **Action**: Scheduling agent automatically books specialized service slots.
4. **Insight**: Failures are traced back to specific factory component batches via RCA.

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
