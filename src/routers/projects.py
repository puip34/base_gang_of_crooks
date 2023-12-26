import fastapi
from server.resolvers import projects

projects_router = fastapi.APIRouter(prefix='/projects', tags=["Projects"])

@projects_router.post(path='/create', response_model=dict)
def create_project(project_name: str, description: str, creator_user_id: int) -> dict:
    return projects.create_project(project_name=project_name, description=description, creator_user_id=creator_user_id)

@projects_router.get(path='/get_all', response_model=dict)
def get_all_projects() -> dict:
    return projects.get_all_projects()
