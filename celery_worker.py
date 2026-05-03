from celery import Celery
import time

# Create Celery app
celery = Celery(
    "brake_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Celery Task with Retry Logic
@celery.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=2,
    retry_kwargs={"max_retries": 3}
)
def brake_decision(self, distance):
    print(f"Task started with distance: {distance}")

    time.sleep(5)

    # 🔴 Simulate failure
    if distance == -1:
        print("❌ Simulated failure... retrying")
        raise Exception("Sensor Failure")

    # 🟢 Normal logic
    if distance < 3:
        result = "Emergency Brake 🚨"
    elif distance < 6:
        result = "Slow Down ⚠️"
    else:
        result = "Safe ✅"

    print(f"✅ Task completed: {result}")
    return result