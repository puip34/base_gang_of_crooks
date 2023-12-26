import fastapi
from server.resolvers import roles

roles_router = fastapi.APIRouter(prefix='/roles', tags=["Roles"])

@roles_router.post(path='/create', response_model=dict)
def create_role(role_name: str) -> dict:
    return roles.create_role(role_name=role_name)

@roles_router.get(path='/get_all', response_model=dict)
def get_all_roles() -> dict:
    return roles.get_all_roles()
