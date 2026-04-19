from fastapi import FastAPI
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_worker import celery, brake_decision

app = FastAPI()

# Input schema
class DistanceInput(BaseModel):
    distance: float


# ✅ Home route (test server)
@app.get("/")
def home():
    return {"message": "Brake Decision System Running 🚗"}


# ✅ Week 3: Trigger Celery Task
@app.post("/trigger-task")
def trigger_task(data: DistanceInput):
    task = brake_decision.delay(data.distance)
    return {
        "task_id": task.id,
        "status": "Processing"
    }


# ✅ Week 4: Check Task Result
@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery)

    if result.state == "PENDING":
        return {"status": "Processing"}
    
    elif result.state == "SUCCESS":
        return {
            "status": "Completed",
            "result": result.result
        }
    
    elif result.state == "FAILURE":
        return {
            "status": "Failed",
            "error": str(result.result)
        }
    
    else:
        return {"status": result.state}