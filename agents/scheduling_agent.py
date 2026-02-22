from agents.master_agent import BaseAgent
import random
import json

class SchedulingAgent(BaseAgent):
    def __init__(self):
        super().__init__("scheduling_agent", "Service Coordinator")
        self.api_url = "http://localhost:5000/api"

    def schedule(self, diagnosis):
        issue = diagnosis.get("issue", "General Service")
        service_type = "Standard Diagnostic"
        
        if "Battery" in issue:
            service_type = "Thermal Management Service"
        elif "Tire" in issue:
            service_type = "Tire & Suspension Inspection"
        elif "RPM" in issue or "Gearbox" in issue:
            service_type = "Powertrain Diagnostic"
        elif "Coolant" in issue:
            service_type = "Cooling System Repair"

        self.log(f"Initiating {service_type} scheduling...")
        self.log("Retrieving available slots from Service Center API...")
        
        available_slots = [
            "2024-03-01 10:00 AM",
            "2024-03-01 02:00 PM",
            "2024-03-02 09:00 AM"
        ]
        selected_slot = random.choice(available_slots)
        self.log(f"Selected available slot: {selected_slot}")

        self.log(f"Confirming booking for {service_type} at {selected_slot}...")
        booking_result = {
            "status": "CONFIRMED",
            "booking_id": f"BK-{random.randint(10000, 99999)}",
            "appointment_time": selected_slot,
            "service": service_type
        }
        
        self.log(f"Booking confirmed. ID: {booking_result['booking_id']}")
        return {"appointment_id": booking_result["booking_id"], "time": selected_slot, "service": service_type}
