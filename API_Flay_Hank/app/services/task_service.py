from app.repositories.tasks_repository import find_by_id, find_all_tasks


def list_tasks():
    return find_all_tasks()

def get_task_by_id(task_id: int):
    return find_by_id(task_id)