# app/models.py
from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from .database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)