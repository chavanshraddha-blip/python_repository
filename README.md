# Brake Decision System (FastAPI + Celery)

This project is a simple backend system that decides braking action based on distance input using asynchronous processing.

## Features
- FastAPI for API endpoints
- Celery for background task processing
- Redis as broker and backend
- Task status tracking using task_id
- Parallel task execution (Week 5)

## API Endpoints

### 1. Home
GET /
- Returns: System running message

### 2. Trigger Task
POST /trigger-task

Request:
{
  "distance": 2
}

Response:
{
  "task_id": "some_id",
  "status": "Processing"
}

### 3. Get Result
GET /result/{task_id}

Response:
{
  "status": "Completed",
  "result": "Emergency Brake 🚨"
}

## Decision Logic
- distance < 3 → Emergency Brake 🚨
- distance < 6 → Slow Down ⚠️
- distance ≥ 6 → Safe ✅

## Week 5: Parallel Processing
In this week, multiple Celery workers were run in parallel using:

celery -A celery_worker.celery worker --loglevel=info --pool=threads --concurrency=4

This allows multiple tasks to execute simultaneously instead of one-by-one.

## How to Run

1. Start Redis
2. Run FastAPI:
   uvicorn main:app --reload
3. Run Celery:
   celery -A celery_worker.celery worker --loglevel=info --pool=threads --concurrency=4
4. Open:
   http://127.0.0.1:8000/docs
   ## 🚀 Run Project (One Click)

Run:
start_project.bat

This will:
- Start FastAPI server
- Start Celery worker (parallel execution)
- Start Flower dashboard
- Open browser automatically

## Outcome
- Learned async task processing
- Implemented Celery with FastAPI
- Executed tasks in parallel
