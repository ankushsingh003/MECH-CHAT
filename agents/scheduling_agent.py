from agents.master_agent import BaseAgent
import random
import json

class SchedulingAgent(BaseAgent):
    def __init__(self):
        super().__init__("scheduling_agent", "Service Coordinator")
        self.api_url = "http://localhost:5000/api"

    def schedule(self, diagnosis):
        self.log("Retrieving available slots from Service Center API...")
        
        # In a real system, we'd use 'requests.get(f"{self.api_url}/slots")'
        # For the demo, we simulate the API response structure
        available_slots = [
            "2024-03-01 10:00 AM",
            "2024-03-01 02:00 PM",
            "2024-03-02 09:00 AM"
        ]
        selected_slot = random.choice(available_slots)
        self.log(f"Selected available slot: {selected_slot}")

        self.log(f"Confirming booking for slot: {selected_slot}...")
        # Simulate POST /api/book
        booking_result = {
            "status": "CONFIRMED",
            "booking_id": f"BK-{random.randint(10000, 99999)}",
            "appointment_time": selected_slot
        }
        
        self.log(f"Booking confirmed. ID: {booking_result['booking_id']}")
        return {"appointment_id": booking_result["booking_id"], "time": selected_slot}
