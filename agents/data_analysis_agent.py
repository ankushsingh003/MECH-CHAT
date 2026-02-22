from agents.master_agent import BaseAgent

class DataAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("data_analysis_agent", "Telemetry Analyst")

    def analyze(self, telemetry):
        self.log(f"Analyzing telemetry: {telemetry}")
        
        anomalies = []
        
        # 1. Battery Temperature
        if telemetry.get("battery_temp", 0) > 80:
            anomalies.append("Battery Overheating")
            
        # 2. Tire Pressure (Expected range 30-35 psi)
        tires = telemetry.get("tire_pressure", [])
        if any(p < 28 or p > 40 for p in tires):
            anomalies.append("Abnormal Tire Pressure")
            
        # 3. Motor RPM
        if telemetry.get("motor_rpm", 0) > 14000:
            anomalies.append("High Motor RPM")
            
        # 4. Coolant Level
        if telemetry.get("coolant_level", 100) < 15:
            anomalies.append("Low Coolant Level")

        if anomalies:
            return {"status": "CRITICAL", "reasons": anomalies}
            
        return {"status": "NORMAL", "reasons": ["All systems within range"]}
