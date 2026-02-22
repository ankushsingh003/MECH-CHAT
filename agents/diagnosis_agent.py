from agents.master_agent import BaseAgent

class DiagnosisAgent(BaseAgent):
    def __init__(self):
        super().__init__("diagnosis_agent", "Failure Predictor")

    def diagnose(self, analysis):
        self.log(f"Diagnosing failure based on: {analysis}")
        if analysis["status"] == "CRITICAL":
            return {
                "issue": analysis["reason"],
                "prediction": "Alternator failure likely in next 48 hours",
                "priority": "HIGH",
                "recommended_action": "Immediate cooling and service check"
            }
        return {"issue": "None", "priority": "LOW"}
