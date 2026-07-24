from app.repositories.tasks_repository import find_by_id, find_all_tasks, add, tasks


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