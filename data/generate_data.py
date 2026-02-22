import json
import random
from datetime import datetime, timedelta

def generate_synthetic_data(num_vehicles=10):
    vehicles = []
    models = ["Model S", "Model X", "Model 3", "Model Y", "Semi", "Cybertruck"]
    
    for i in range(num_vehicles):
        v_id = f"VIN-{1000 + i}"
        v_data = {
            "id": v_id,
            "model": random.choice(models),
            "mileage": random.randint(5000, 80000),
            "last_service": (datetime.now() - timedelta(days=random.randint(30, 180))).strftime("%Y-%m-%d"),
            "health_score": random.randint(70, 100),
            "telemetry": {
                "battery_temp": random.uniform(20.0, 45.0),
                "tire_pressure": [random.uniform(30.0, 35.0) for _ in range(4)],
                "motor_rpm": random.randint(0, 15000),
                "coolant_level": random.uniform(80.0, 100.0)
            },
            "history": [
                {"date": "2023-11-15", "issue": "Tire Rotation", "cost": 50},
                {"date": "2024-01-10", "issue": "Software Update", "cost": 0}
            ]
        }
        # Inject one failure for demonstration
        if i == 0:
            v_data["telemetry"]["battery_temp"] = 85.5 # Overheating
            v_data["health_score"] = 45
        
        vehicles.append(v_data)
        
    return vehicles

if __name__ == "__main__":
    data = generate_synthetic_data(num_vehicles=210)
    with open("data/vehicles.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Synthetic vehicle data generated successfully.")
