import time

class UEBAMonitor:
    def __init__(self):
        self.logs = []

    def audit(self, agent_name, action, details):
        log_entry = {
            "timestamp": time.time(),
            "agent": agent_name,
            "action": action,
            "details": details,
            "status": "APPROVED"
        }
        
        # Simple anomaly detection: suspicious activity if scheduling without diagnosis
        if action == "SCHEDULE_APPOINTMENT" and "DIAGNOSIS_ID" not in details:
            log_entry["status"] = "FLAGGED_UNAUTHORIZED"
            print(f"!!! SECURITY ALERT: Unauthorized scheduling attempt by {agent_name} !!!")
        
        self.logs.append(log_entry)
        return log_entry["status"]

    def get_audit_report(self):
        return self.logs
