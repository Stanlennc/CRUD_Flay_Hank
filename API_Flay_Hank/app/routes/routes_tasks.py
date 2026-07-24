
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.services.task_service import list_tasks, get_task_by_id

router = APIRouter()

@router.get("/tasks")
def list_tasks_service():
    return list_tasks()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": "Task 99 not found"})
    return get_task_by_id(task_id)
   