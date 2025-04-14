# app/main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .models import SensorData
from .database import engine, SessionLocal
from .database import Base
from .sensor_sim import generate_fake_data
import threading
import time

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
Base.metadata.create_all(bind=engine)

# Tạo luồng riêng để cập nhật dữ liệu mỗi 5 giây
def sensor_thread():
    while True:
        generate_fake_data()
        time.sleep(5)

threading.Thread(target=sensor_thread, daemon=True).start()

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    db = SessionLocal()
    data = db.query(SensorData).order_by(SensorData.timestamp.desc()).limit(20).all()
    db.close()
    data = list(reversed(data))  # Đảo lại để hiển thị từ cũ đến mới
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})