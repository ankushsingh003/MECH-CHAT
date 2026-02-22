from agents.master_agent import BaseAgent
import random

class SchedulingAgent(BaseAgent):
    def __init__(self):
        super().__init__("scheduling_agent", "Service Coordinator")

    def schedule(self, diagnosis):
        self.log("Retrieving available slots from Service Center API...")
        slot = "2024-03-01 10:00 AM"
        self.log(f"Booking slot: {slot}")
        return {"appointment_id": f"APP-{random.randint(1000, 9999)}", "time": slot}
