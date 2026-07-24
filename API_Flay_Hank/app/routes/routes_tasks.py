
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.services.task_service import list_tasks, get_task_by_id, InvalidTaskError, create_task
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str | None = None

router = APIRouter()

@router.get("/all_tasks")
def list_tasks_service():
    return list_tasks()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": "Task 99 not found"})
    return get_task_by_id(task_id)

@router.post("/tasks", status_code=201, )
def create_new_task(new_task: TaskCreate ):
    try:
        return create_task(new_task.model_dump())
    except InvalidTaskError as e:
        raise HTTPException(status_code=400, detail={"error": str(e)})