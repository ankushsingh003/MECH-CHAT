from agents.master_agent import BaseAgent

class DataAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("data_analysis_agent", "Telemetry Analyst")

    def analyze(self, telemetry):
        self.log(f"Analyzing telemetry: {telemetry}")
        # Simple anomaly detection
        if telemetry.get("battery_temp", 0) > 80:
            return {"status": "CRITICAL", "reason": "Battery Overheating"}
        return {"status": "NORMAL", "reason": "All systems within range"}
