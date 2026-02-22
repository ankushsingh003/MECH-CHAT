from agents.master_agent import BaseAgent

class FeedbackAgent(BaseAgent):
    def __init__(self):
        super().__init__("feedback_agent", "Quality Monitor")

    def collect_feedback(self, booking):
        self.log(f"Collecting feedback for booking: {booking['appointment_id']}")
        return {"rating": 5, "comments": "Proactive alert saved my battery!"}
