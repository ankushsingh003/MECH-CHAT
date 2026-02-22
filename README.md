# MECH-CHAT | Agentic Fleet Control Center

MECH-CHAT is a premium, full-stack agentic orchestration system designed for high-performance vehicle fleet management. It leverages a multi-agent architecture to monitor telemetry, diagnose failures, and coordinate maintenance workflows with zero manual intervention.

![MECH-CHAT Dashboard](dashboard/preview.png) *(Placeholder if you have a screenshot)*

## 🏗️ System Architecture & Orchestration

Instead of long manuals, here is how MECH-CHAT orchestrates your fleet:

```mermaid
flowchart TD
    subgraph "Dashboard (User Interface)"
        UI[Premium Fleet Dashboard]
        Logs[Live Orchestration Feed]
        SAPI[SAPI Voice interface]
    end

    subgraph "Master Orchestrator"
        MO{Orchestrator}
        Audit[UEBA Security Monitor]
    end

    subgraph "Specialized Agents"
        AA[Data Analysis Agent]
        DA[Diagnosis Agent]
        EA[Engagement Agent]
        SA[Scheduling Agent]
        FA[Feedback Agent]
        IA[Manufacturing Insights]
    end

    UI -->|Trigger| MO
    MO -->|1. Analyze| AA
    MO -->|2. Diagnose| DA
    MO -->|3. Alert| EA
    MO -->|4. Schedule| SA
    MO -->|5. Verify| FA
    MO -->|6. RCA| IA

    EA <-->|Voice Alert| SAPI
    AA & DA & EA & SA & FA & IA -->|Real-time Logs| Logs
    MO -.->|Compliance Audit| Audit

    style UI fill:#030508,stroke:#00f2ff,stroke-width:2px,color:#fff
    style MO fill:#0a0f19,stroke:#00f2ff,stroke-width:4px,color:#fff
    style AA,DA,EA,SA,FA,IA fill:#111,stroke:#94a3b8,color:#f1f5f9
    style Audit fill:#ff4d4d,stroke:#fff,color:#fff
```

### 🚀 High-Level Workflow
1. **Detection**: Analysts monitor Heat, Tires, RPM, and Coolant.
2. **Alert**: SAPI interface engages the driver with personalized voice alerts.
3. **Action**: Scheduling agent automatically books specialized service slots.
4. **Insight**: Failures are traced back to specific factory component batches.

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
