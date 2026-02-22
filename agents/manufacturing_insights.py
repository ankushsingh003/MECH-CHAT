from agents.master_agent import BaseAgent

class ManufacturingInsightsModule(BaseAgent):
    def __init__(self):
        super().__init__("manufacturing_insights", "RCA/CAPA Analyst")

    def generate_insight(self, diagnosis, feedback):
        self.log("Synthesizing RCA data for manufacturing team...")
        issue = diagnosis.get("issue", "Unknown")
        
        component = "General Systems"
        root_cause = "Unknown technical anomaly"
        recommendation = "Full batch inspection recommended"
        
        if "Battery" in issue:
            component = "Battery Cooling System"
            root_cause = "Potential soldering defect in batch #402"
            recommendation = "Inspect cooling fans in upcoming production"
        elif "Tire" in issue:
            component = "Tire/Sensor Assembly"
            root_cause = "Sealant degradation in Q3 components"
            recommendation = "Switch to reinforced gaskets for next cycle"
        elif "RPM" in issue or "Gearbox" in issue:
            component = "Drive Inverter/Gearbox"
            root_cause = "Tolerances slightly off in CNC milling"
            recommendation = "Recalibrate machining centers for tighter tolerances"
        elif "Coolant" in issue:
            component = "Fluid Loop Seals"
            root_cause = "Material fatigue in high-temp hoses"
            recommendation = "Upgrade to high-grade silicone hoses"

        insight = {
            "component": component,
            "root_cause": root_cause,
            "recommendation": recommendation,
            "feedback_rating": feedback.get("rating")
        }
        self.log(f"Generated insight for {component}: {insight}")
        return insight
