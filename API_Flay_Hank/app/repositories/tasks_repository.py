


SEED_TASKS = [
    {"id": 1, "title": "Code at night", "done": True},
    {"id": 2, "title": "Run at the park", "done": False},
    {"id": 3, "title": "Have a lunch", "done": True},
]


tasks = [task.copy() for task in SEED_TASKS]

def find_all_tasks():
    return [task.copy() for task in tasks]

def find_by_id(task_id: int) -> dict | None:
    task = next((t for t in tasks if t["id"] == task_id), None)
    return task.copy() if task else None

def add(new_task: dict) -> dict:
    tasks.append(new_task)
    return new_task

# repository.py
def update_task(task_id: int, updated_fields: dict) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_fields)
            return task
    return None

def delete_task_repository(task_id: int) -> bool:
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False