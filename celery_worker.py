from celery import Celery
import time

celery = Celery(
    "brake_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task(bind=True, max_retries=3)
def brake_decision(self, distance):
    print(f"🚗 Task started with distance: {distance}")

    # Simulate failure
    if distance < 0:
        print("❌ Sensor failure! Retrying...")
        try:
            raise Exception("Sensor Failure")
        except Exception as exc:
            raise self.retry(exc=exc, countdown=2)

    time.sleep(5)

    if distance < 3:
        return "Emergency Brake 🚨"
    elif distance < 6:
        return "Slow Down ⚠️"
    else:
        return "Safe ✅"