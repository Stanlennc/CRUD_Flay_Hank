from app.repositories.tasks_repository import find_by_id, find_all_tasks, add, tasks, update_task, delete_task_repository


def list_tasks():
    return find_all_tasks()

def get_task_by_id(task_id: int):
    return find_by_id(task_id)

class InvalidTaskError(Exception):
    pass

def create_task(data: dict) -> dict:
    title = data.get("title", "").strip()
    if not title:
        raise InvalidTaskError("Title is required")
    existing_tasks = find_all_tasks()
    new_id = max((t["id"] for t in existing_tasks), default=0) +1
    new_task = {
        "id": new_id,
        "title": title,
        "done": False
    }
    return add(new_task)

def update_task_service(task_id: int, updated_task: dict) -> dict | None:
    existing_tasks = find_all_tasks()

    for task in existing_tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.get("title", task["title"]).strip()
            task["done"] = updated_task.get("done", task["done"])
            return task

    return None  

def delete_task_service(task_id: int) -> bool:
    existing_tasks = find_all_tasks()
    for i, task in enumerate(existing_tasks):
        if task["id"] == task_id:
            del existing_tasks[i]
            return True
    return False
           