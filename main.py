from fastapi import FastAPI
from pydantic import BaseModel
from celery_worker import brake_decision

app = FastAPI()

class DistanceInput(BaseModel):
    distance: int

@app.get("/")
def home():
    return {"message": "Brake Decision System Running 🚗"}

@app.post("/trigger-task")
def trigger_task(data: DistanceInput):
    task = brake_decision.delay(data.distance)
    return {"task_id": task.id}