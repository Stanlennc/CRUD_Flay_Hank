
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.services.task_service import list_tasks, get_task_by_id, InvalidTaskError, create_task, update_task_service, delete_task_service
from pydantic import BaseModel
from fastapi.responses import Response


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

@router.put("/tasks/{task_id}")
def update_task_route(task_id: int, body: TaskCreate):
    if not body.title or not body.title.strip():
        raise HTTPException(status_code=400, detail="Body is empty or title is missing!")

    updated = update_task_service(task_id, body.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = delete_task_service(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)