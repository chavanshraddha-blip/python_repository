from celery import Celery

celery = Celery(
    "brake_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def brake_decision(distance):
    if distance < 3:
        return "Emergency Brake 🚨"
    elif distance < 6:
        return "Slow Down ⚠️"
    else:
        return "Safe ✅"