from agents.master_agent import BaseAgent

class CustomerEngagementAgent(BaseAgent):
    def __init__(self):
        super().__init__("customer_engagement_agent", "Voice Interface")

    def engage(self, diagnosis):
        issue = diagnosis.get("issue", "system anomaly")
        self.log(f"Initiating customer engagement for: {issue}")
        
        message = f"SAPI Alert: {issue} detected. {diagnosis.get('prediction', '')}. {diagnosis.get('recommended_action', '')}. Would you like to schedule a service?"
        self.log(f"Broadcasting via SAPI: {message}")
        
        return {
            "confirmed": True, 
            "communication_channel": "SAPI_VOICE",
            "message": message
        }
