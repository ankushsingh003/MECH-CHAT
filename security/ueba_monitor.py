import time
import requests

class UEBAMonitor:
    def __init__(self):
        self.logs = []
        self.api_base = "http://localhost:5000/api/dashboard"
        self.audit_callback = None # Set this to log directly to memory

    def audit(self, agent_name, action, details):
        log_entry = {
            "timestamp": time.time(),
            "agent": agent_name,
            "action": action,
            "details": details,
            "status": "APPROVED"
        }
        
        # Simple anomaly detection
        if action == "SCHEDULE_APPOINTMENT" and "DIAGNOSIS_ID" not in details:
            log_entry["status"] = "FLAGGED_UNAUTHORIZED"

        if self.audit_callback:
            self.audit_callback(log_entry)
        else:
            try:
                requests.post(f"{self.api_base}/audits", json=log_entry)
            except:
                pass
            
        self.logs.append(log_entry)
        return log_entry["status"]

    def get_audit_report(self):
        return self.logs
