from agents.master_agent import MasterAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.customer_engagement_agent import CustomerEngagementAgent
from agents.scheduling_agent import SchedulingAgent
from agents.feedback_agent import FeedbackAgent
from agents.manufacturing_insights import ManufacturingInsightsModule
from sapi.sapi_bridge import SAPIBridge, simulate_voice_conversation
from security.ueba_monitor import UEBAMonitor
import json

def main():
    print("=== Agentic AI Vehicle Maintenance Workflow Demo ===")
    
    # Initialize Components
    master = MasterAgent()
    analysis_agent = DataAnalysisAgent()
    diagnosis_agent = DiagnosisAgent()
    engagement_agent = CustomerEngagementAgent()
    scheduling_agent = SchedulingAgent()
    feedback_agent = FeedbackAgent()
    insights_module = ManufacturingInsightsModule()
    
    ueba = UEBAMonitor()
    sapi = SAPIBridge()

    # Register Workers
    master.register_worker("data_analysis_agent", analysis_agent)
    master.register_worker("diagnosis_agent", diagnosis_agent)
    master.register_worker("customer_engagement_agent", engagement_agent)
    master.register_worker("scheduling_agent", scheduling_agent)
    master.register_worker("feedback_agent", feedback_agent)
    master.register_worker("manufacturing_insights", insights_module)

    # Load Mock Telemetry for Problematic Vehicle
    with open("data/vehicles.json", "r") as f:
        vehicles = json.load(f)
    
    problem_vehicle = vehicles[0] # VIN-1000 with heating issue
    print(f"\nMonitoring vehicle: {problem_vehicle['id']} ({problem_vehicle['model']})")

    # Step 1: Security Audit for Monitoring Action
    ueba.audit("MasterOrchestrator", "TELEMETRY_MONITOR", {"vin": problem_vehicle["id"]})

    # Step 2: Orchestrate Workflow
    master.orchestrate("TELEMETRY_ANOMALY", problem_vehicle["telemetry"])

    # Step 3: Specific SAPI Voice Simulation (Normally triggered by Engagement Agent)
    print("\n--- SAPI Voice Interaction Simulation ---")
    diag_results = {
        "issue": "Critical Battery Overheating",
        "priority": "HIGH"
    }
    confirmed = simulate_voice_conversation(sapi, diag_results)
    
    if confirmed:
        ueba.audit("SchedulingAgent", "SCHEDULE_APPOINTMENT", {"vin": problem_vehicle["id"], "DIAGNOSIS_ID": "D-101"})
        print("\nWorkflow successful. Check audits for compliance.")

if __name__ == "__main__":
    main()
