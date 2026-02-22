import json
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from agents.master_agent import MasterAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.customer_engagement_agent import CustomerEngagementAgent
from agents.scheduling_agent import SchedulingAgent
from agents.feedback_agent import FeedbackAgent
from agents.manufacturing_insights import ManufacturingInsightsModule
from security.ueba_monitor import UEBAMonitor

app = Flask(__name__)
CORS(app) # Enable CORS for dashboard

# Initialize Agentic Engine
master = MasterAgent()
ueba = UEBAMonitor()

# Register Workers
master.register_worker("data_analysis_agent", DataAnalysisAgent())
master.register_worker("diagnosis_agent", DiagnosisAgent())
master.register_worker("customer_engagement_agent", CustomerEngagementAgent())
master.register_worker("scheduling_agent", SchedulingAgent())
master.register_worker("feedback_agent", FeedbackAgent())
master.register_worker("manufacturing_insights", ManufacturingInsightsModule())

# In-memory storage for dashboard live data
orchestration_logs = []
audit_logs = []

@app.route("/api/trigger/<vin>", methods=["POST"])
def trigger_orchestration(vin):
    vehicle = next((v for v in vehicles if v["id"] == vin), None)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    
    # Run Orchestration
    # First, a security audit
    ueba.audit("MasterOrchestrator", "INTERACTIVE_TRIGGER", {"vin": vin})
    
    # Run the main orchestration
    master.orchestrate("TELEMETRY_ANOMALY", vehicle["telemetry"])
    
    return jsonify({"status": "ORCHESTRATION_STARTED", "vin": vin})

# Load initial data
with open("data/vehicles.json", "r") as f:
    vehicles = json.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the MECH-CHAT Mock Server!",
        "endpoints": {
            "vehicles": "/api/vehicles",
            "telemetry": "/api/telemetry/<vin>",
            "maintenance": "/api/maintenance/<vin>",
            "slots": "/api/slots",
            "book": "/api/book [POST]"
        }
    })

@app.route("/api/telemetry/<vin>", methods=["GET"])
def get_telemetry(vin):
    vehicle = next((v for v in vehicles if v["id"] == vin), None)
    if vehicle:
        # Simulate real-time variation
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
    # Mock available slots for the next few days
    slots = [
        "2024-03-01 10:00 AM",
        "2024-03-01 02:00 PM",
        "2024-03-02 09:00 AM",
        "2024-03-02 11:30 AM"
    ]
    return jsonify({"available_slots": slots})

@app.route("/api/book", methods=["POST"])
def book_appointment():
    # In a real app, we'd take VIN and slot from request.json
    return jsonify({
        "status": "CONFIRMED",
        "booking_id": f"BK-{random.randint(10000, 99999)}",
        "message": "Appointment successfully scheduled."
    })

@app.route("/api/dashboard/logs", methods=["GET", "POST"])
def manage_logs():
    if request.method == "POST":
        log_entry = request.json
        orchestration_logs.append(log_entry)
        if len(orchestration_logs) > 50: orchestration_logs.pop(0)
        return jsonify({"status": "OK"})
    return jsonify(orchestration_logs)

@app.route("/api/dashboard/audits", methods=["GET", "POST"])
def manage_audits():
    if request.method == "POST":
        audit_entry = request.json
        audit_logs.append(audit_entry)
        if len(audit_logs) > 50: audit_logs.pop(0)
        return jsonify({"status": "OK"})
    return jsonify(audit_logs)

if __name__ == "__main__":
    app.run(port=5000)
