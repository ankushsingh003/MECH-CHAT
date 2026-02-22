from agents.master_agent import BaseAgent

class DiagnosisAgent(BaseAgent):
    def __init__(self):
        super().__init__("diagnosis_agent", "Failure Predictor")

    def diagnose(self, analysis):
        self.log(f"Diagnosing failure based on: {analysis}")
        
        if analysis["status"] == "CRITICAL":
            reasons = analysis.get("reasons", [])
            primary_reason = reasons[0] if reasons else "Unknown"
            
            diagnosis = {
                "issue": primary_reason,
                "priority": "HIGH"
            }
            
            if "Battery Overheating" in reasons:
                diagnosis.update({
                    "prediction": "Alternator failure likely in next 48 hours",
                    "recommended_action": "Immediate cooling and service check"
                })
            elif "Abnormal Tire Pressure" in reasons:
                diagnosis.update({
                    "prediction": "Potential tire puncture or sensor failure",
                    "recommended_action": "Check tire pressure manually and inspect for punctures"
                })
            elif "High Motor RPM" in reasons:
                diagnosis.update({
                    "prediction": "Gearbox/Transmission slippage detected",
                    "recommended_action": "Avoid high speeds and schedule transmission inspection"
                })
            elif "Low Coolant Level" in reasons:
                diagnosis.update({
                    "prediction": "Cooling system leak or pump failure",
                    "recommended_action": "Refill coolant and check for leaks immediately"
                })
            else:
                diagnosis.update({
                    "prediction": "Undetermined system failure",
                    "recommended_action": "Full system diagnostic required"
                })
                
            return diagnosis
            
        return {"issue": "None", "priority": "LOW"}
