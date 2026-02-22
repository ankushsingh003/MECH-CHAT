interface Vehicle {
    id: string;
    model: string;
    health_score: number;
    telemetry: any;
}

interface LogEntry {
    agent: string;
    role: string;
    message: string;
    timestamp: number;
}

interface AuditEntry {
    agent: string;
    action: string;
    status: string;
    timestamp: number;
}

const API_BASE = "http://localhost:5000/api";

async function fetchData(endpoint: string) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`);
        return await response.json();
    } catch (err) {
        console.error(`Error fetching ${endpoint}:`, err);
        return null;
    }
}

function updateFleet(vehicles: Vehicle[]) {
    const container = document.getElementById("fleet-container");
    if (!container || !vehicles) return;

    container.innerHTML = vehicles.map(v => `
    <div class="vehicle-item" onclick="triggerOrchestration('${v.id}')" data-vin="${v.id}">
      <div class="vehicle-info">
        <span class="vin">${v.id}</span>
        <span class="model">${v.model}</span>
      </div>
      <div class="health-bar">
        <div class="health-fill" style="width: ${v.health_score}%; background: ${v.health_score > 80 ? '#00ff88' : v.health_score > 60 ? '#ffcc00' : '#ff4d4d'}"></div>
      </div>
    </div>
  `).join("");
}

async function triggerOrchestration(vin: string) {
    console.log(`Triggering AI for: ${vin}`);

    // Visual feedback
    const items = document.querySelectorAll(".vehicle-item");
    items.forEach(i => i.classList.remove("active"));
    const selected = document.querySelector(`[data-vin="${vin}"]`);
    if (selected) selected.classList.add("active");

    try {
        const res = await fetch(`${API_BASE}/trigger/${vin}`, { method: 'POST' });
        const data = await res.json();
        console.log("Orchestration Response:", data);
    } catch (err) {
        console.error("Trigger Failed:", err);
    }
}

// @ts-ignore - expose to HTML
window.triggerOrchestration = triggerOrchestration;

function updateLogs(logs: LogEntry[]) {
    const container = document.getElementById("log-container");
    if (!container || !logs) return;

    if (logs.length === 0) {
        container.innerHTML = '<div class="empty-state">No active orchestration tasks</div>';
        return;
    }

    container.innerHTML = logs.sort((a, b) => b.timestamp - a.timestamp).map(l => `
    <div class="log-entry">
      <span class="timestamp">${new Date(l.timestamp * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })}</span>
      <span class="agent-name">[${l.agent}]</span> ${l.message}
    </div>
  `).join("");

    // Update SAPI Chat with the latest engagement message
    const engagementLog = logs.find(l => l.agent === "customer_engagement_agent");
    if (engagementLog) {
        const chatContainer = document.getElementById("sapi-container");
        if (chatContainer) {
            chatContainer.innerHTML = `<div class="chat-bubble bot">${engagementLog.message}</div>`;
        }
    }
}

function updateAudits(audits: AuditEntry[]) {
    const container = document.getElementById("audit-container");
    if (!container || !audits) return;

    if (audits.length === 0) {
        container.innerHTML = '<div class="empty-state">System secure. No alerts.</div>';
        return;
    }

    container.innerHTML = audits.sort((a, b) => b.timestamp - a.timestamp).map(a => `
    <div class="log-entry">
      <span class="timestamp">${new Date(a.timestamp * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
      <span class="agent-name">${a.agent}</span> 
      <span class="status-${a.status.toLowerCase().includes('flagged') ? 'flagged' : 'approved'}">${a.status}</span>: ${a.action}
    </div>
  `).join("");
}

async function loop() {
    const vehicles = await fetchData("/vehicles");
    const logs = await fetchData("/dashboard/logs");
    const audits = await fetchData("/dashboard/audits");

    if (vehicles) updateFleet(vehicles.slice(0, 50)); // Limit to first 50 for performance
    if (logs) updateLogs(logs);
    if (audits) updateAudits(audits);

    setTimeout(loop, 2000);
}

// Initial Call
loop();
console.log("MECH-CHAT Dashboard Initialized");
