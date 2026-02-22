import json
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Load initial data
with open("data/vehicles.json", "r") as f:
    vehicles = json.load(f)

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

if __name__ == "__main__":
    app.run(port=5000)
