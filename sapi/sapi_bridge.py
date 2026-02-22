class SAPIBridge:
    def __init__(self):
        print("[SAPI] Initializing Speech/System API Bridge...")

    def speak(self, text):
        print(f"[SAPI VOICE]: {text}")

    def notify(self, vin, priority, message):
        print(f"[SAPI NOTIFY] [{vin}] Priority: {priority} - {message}")

    def capture_intent(self):
        # Simulated voice intent capture
        print("[SAPI] Waiting for user voice response...")
        return "YES_CONFIRM_SERVICE"

# Mock SAPI workflow
def simulate_voice_conversation(bridge, diag_info):
    bridge.speak(f"Hello! Your vehicle is reporting a {diag_info['issue']}.")
    bridge.speak(f"I recommend scheduling a service appointment. Would you like to proceed?")
    intent = bridge.capture_intent()
    if intent == "YES_CONFIRM_SERVICE":
        bridge.speak("Great! I have reserved a slot for you next Monday.")
        return True
    return False
