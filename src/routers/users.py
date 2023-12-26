import fastapi
from server.resolvers import users

users_router = fastapi.APIRouter(prefix='/users', tags=["Users"])

@users_router.post(path='/create', response_model=dict)
def create_user(username: str, email: str) -> dict:
    return users.create_user(username=username, email=email)

@users_router.get(path='/get_all', response_model=dict)
def get_all_users() -> dict:
    return users.get_all_users()
