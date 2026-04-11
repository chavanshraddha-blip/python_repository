from fastapi import FastAPI
from celery_worker import brake_decision

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Brake Decision System Running 🚗"}

@app.get("/check/{distance}")
def check(distance: int):
    task = brake_decision.delay(distance)
    return {
        "task_id": task.id,
        "status": "Processing"
    }