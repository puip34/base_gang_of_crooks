import fastapi
from server.resolvers import tasks

tasks_router = fastapi.APIRouter(prefix='/tasks', tags=["Tasks"])

@tasks_router.post(path='/create', response_model=dict)
def create_task(task_name: str, description: str, project_id: int, creator_user_id: int, assignee_user_id: int) -> dict:
    return tasks.create_task(task_name=task_name, description=description, project_id=project_id, creator_user_id=creator_user_id, assignee_user_id=assignee_user_id)

@tasks_router.get(path='/get_all', response_model=dict)
def get_all_tasks() -> dict:
    return tasks.get_all_tasks()
