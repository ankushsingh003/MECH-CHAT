import time

class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def log(self, message):
        print(f"[{self.name}] ({self.role}): {message}")

class MasterAgent(BaseAgent):
    def __init__(self):
        super().__init__("MasterOrchestrator", "Main Orchestrator")
        self.workers = {}

    def register_worker(self, agent_name, agent_instance):
        self.workers[agent_name] = agent_instance
        self.log(f"Registered worker: {agent_name}")

    def orchestrate(self, task_type, data):
        self.log(f"Orchestrating task: {task_type}")
        if task_type == "TELEMETRY_ANOMALY":
            # 1. Ask Analysis Agent for details
            analysis = self.workers["data_analysis_agent"].analyze(data)
            self.log(f"Analysis complete: {analysis}")
            
            # 2. Ask Diagnosis Agent for prediction
            diagnosis = self.workers["diagnosis_agent"].diagnose(analysis)
            self.log(f"Diagnosis complete: {diagnosis}")
            
            # 3. Trigger Customer Engagement if priority is high
            if diagnosis["priority"] == "HIGH":
                engagement = self.workers["customer_engagement_agent"].engage(diagnosis)
                self.log(f"Engagement started: {engagement}")
                
                # 4. If engagement confirms, trigger Scheduling
                if engagement["confirmed"]:
                    booking = self.workers["scheduling_agent"].schedule(diagnosis)
                    self.log(f"Booking complete: {booking}")
                    
                    # 5. Follow up after service (simulated)
                    feedback = self.workers["feedback_agent"].collect_feedback(booking)
                    self.log(f"Feedback collected: {feedback}")
                    
                    # 6. Feed to Manufacturing Quality Insights
                    self.workers["manufacturing_insights"].generate_insight(diagnosis, feedback)
        
        return "Workflow executed successfully"
