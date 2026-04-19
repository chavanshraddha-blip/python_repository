from celery import Celery
import time

celery = Celery(
    "brake_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def brake_decision(distance):
    time.sleep(5)  

    if distance < 3:
        return "Emergency Brake 🚨"
    elif distance < 6:
        return "Slow Down ⚠️"
    else:
        return "Safe ✅"