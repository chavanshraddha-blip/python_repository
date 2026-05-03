# 🚗 Brake Decision System (FastAPI + Celery)

A backend system that determines braking action based on distance input using asynchronous task processing.

This project uses:

* **FastAPI** for API development
* **Celery** for background task processing
* **Redis** as message broker and result backend
* **Flower** for monitoring tasks

## ⚙️ Features

* FastAPI-based REST API
* Asynchronous task execution using Celery
* Parallel processing with multiple workers
* Retry mechanism for handling failures
* Real-time monitoring using Flower dashboard
* One-click project startup using batch script

## 🛠️ Tech Stack

* Python
* FastAPI
* Celery
* Redis
* Flower

## 🚀 How to Run (Manual)

1. Start Redis server
2. Run FastAPI:

   uvicorn main:app --reload
  
3. Run Celery worker:

   celery -A celery_worker.celery worker --loglevel=info --pool=threads --concurrency=4

4. Run Flower dashboard:

   celery -A celery_worker.celery flower --port=5556

5. Open in browser:

   * FastAPI Docs → http://127.0.0.1:8000/docs
   * Flower Dashboard → http://localhost:5556

##  Run Project (One Click)

Run:

start_project.bat


This will:

* Start FastAPI server
* Start Celery worker (parallel execution)
* Start Flower dashboard
* Open browser automatically

##  API Endpoints

###  Trigger Task

**POST** `/trigger-task`

Request:

```json
{
  "distance": 2
}
```

Response:

```json
{
  "task_id": "xxxx",
  "status": "Processing"
}
```

---

###  Get Result

**GET** `/result/{task_id}`

Response (Success):

```json
{
  "status": "Completed",
  "result": "Emergency Brake 🚨"
}
```

Response (Failure):

```json
{
  "status": "Failed",
  "error": "Sensor Failure"
}
```

---

##  Retry Mechanism

* If `distance < 0`, system simulates sensor failure
* Task automatically retries (max 3 times)
* Uses Celery retry with delay

---

##  Monitoring

Flower dashboard allows:

* Viewing active tasks
* Tracking retries and failures
* Monitoring worker performance

---

##  Outcome

* Built asynchronous backend system
* Implemented task queue using Celery + Redis
* Enabled parallel task execution
* Implemented retry mechanism for failure handling
* Integrated monitoring using Flower
* Automated full system startup

---

##  Project Structure

```
python_repository/
│── main.py
│── celery_worker.py
│── start_project.bat
│── README.md
│── venv/
```

---

##  Author

Shraddha Chavan

