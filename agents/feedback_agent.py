from agents.master_agent import BaseAgent

class FeedbackAgent(BaseAgent):
    def __init__(self):
        super().__init__("feedback_agent", "Quality Monitor")

    def collect_feedback(self, booking):
        service = booking.get("service", "service")
        self.log(f"Collecting feedback for booking: {booking['appointment_id']} ({service})")
        
        return {
            "rating": 5, 
            "comments": f"The proactive alert for {service} saved my vehicle from major damage!"
        }
