# app/sensor_sim.py
import random
from datetime import datetime
from .models import SensorData
from .database import SessionLocal

def generate_fake_data():
    db = SessionLocal()
    temp = random.uniform(40, 80)  # Nhiệt độ từ 40°C đến 80°C
    data = SensorData(temperature=temp)
    db.add(data)
    db.commit()
    db.close()
    print(f"[{datetime.now()}] Nhiệt độ: {temp:.2f}°C")