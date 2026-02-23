import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from agents.master_agent import MasterAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.customer_engagement_agent import CustomerEngagementAgent
from agents.scheduling_agent import SchedulingAgent
from agents.feedback_agent import FeedbackAgent
from agents.manufacturing_insights import ManufacturingInsightsModule
from security.ueba_monitor import UEBAMonitor

app = Flask(__name__, static_folder='../dashboard/dist', static_url_path='/')
CORS(app) # Enable CORS for dashboard

# In-memory storage for dashboard live data
orchestration_logs = []
audit_logs = []

def local_log(entry):
    orchestration_logs.append(entry)
    if len(orchestration_logs) > 50: orchestration_logs.pop(0)

def local_audit(entry):
    audit_logs.append(entry)
    if len(audit_logs) > 50: audit_logs.pop(0)

# Initialize Agentic Engine
master = MasterAgent()
master.logger_callback = local_log
ueba = UEBAMonitor()
ueba.audit_callback = local_audit

# Register Workers
def register_worker(name, instance):
    instance.logger_callback = local_log
    master.register_worker(name, instance)

register_worker("data_analysis_agent", DataAnalysisAgent())
register_worker("diagnosis_agent", DiagnosisAgent())
register_worker("customer_engagement_agent", CustomerEngagementAgent())
register_worker("scheduling_agent", SchedulingAgent())
register_worker("feedback_agent", FeedbackAgent())
register_worker("manufacturing_insights", ManufacturingInsightsModule())

import threading

@app.route("/api/trigger/<vin>", methods=["POST"])
def trigger_orchestration(vin):
    vehicle = next((v for v in vehicles if v["id"] == vin), None)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    
    def run_async():
        ueba.audit("MasterOrchestrator", "INTERACTIVE_TRIGGER", {"vin": vin})
        master.orchestrate("TELEMETRY_ANOMALY", vehicle["telemetry"])

    threading.Thread(target=run_async).start()
    return jsonify({"status": "ORCHESTRATION_STARTED", "vin": vin})

# Load initial data
with open("data/vehicles.json", "r") as f:
    vehicles = json.load(f)

# Serve Dashboard
@app.route("/")
def serve_dashboard():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/<path:path>")
def serve_assets(path):
    if path.startswith("api/"): # Fallback for API routes if needed
        return None 
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api/telemetry/<vin>", methods=["GET"])
def get_telemetry(vin):
    vehicle = next((v for v in vehicles if v["id"] == vin), None)
    if vehicle:
        vehicle["telemetry"]["motor_rpm"] = random.randint(2000, 8000)
        return jsonify(vehicle["telemetry"])
    return jsonify({"error": "Vehicle not found"}), 404

@app.route("/api/maintenance/<vin>", methods=["GET"])
def get_maintenance(vin):
    vehicle = next((v for v in vehicles if v["id"] == vin), None)
    if vehicle:
        return jsonify(vehicle["history"])
    return jsonify({"error": "Vehicle not found"}), 404

@app.route("/api/vehicles", methods=["GET"])
def list_vehicles():
    return jsonify(vehicles)

@app.route("/api/slots", methods=["GET"])
def get_slots():
    slots = ["2024-03-01 10:00 AM", "2024-03-01 02:00 PM", "2024-03-02 09:00 AM", "2024-03-02 11:30 AM"]
    return jsonify({"available_slots": slots})

@app.route("/api/book", methods=["POST"])
def book_appointment():
    return jsonify({
        "status": "CONFIRMED",
        "booking_id": f"BK-{random.randint(10000, 99999)}",
        "message": "Appointment successfully scheduled."
    })

@app.route("/api/dashboard/logs", methods=["GET", "POST", "DELETE"])
def manage_logs():
    if request.method == "POST":
        local_log(request.json)
        return jsonify({"status": "OK"})
    elif request.method == "DELETE":
        orchestration_logs.clear()
        return jsonify({"status": "CLEARED"})
    return jsonify(orchestration_logs)

@app.route("/api/dashboard/audits", methods=["GET", "POST"])
def manage_audits():
    if request.method == "POST":
        local_audit(request.json)
        return jsonify({"status": "OK"})
    return jsonify(audit_logs)

if __name__ == "__main__":
    app.run(port=5000, threaded=True)
