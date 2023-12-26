import fastapi
from server.resolvers import comments

comments_router = fastapi.APIRouter(prefix='/comments', tags=["Comments"])

@comments_router.post(path='/create', response_model=dict)
def create_comment(task_id: int, user_id: int, comment_text: str) -> dict:
    return comments.create_comment(task_id=task_id, user_id=user_id, comment_text=comment_text)

@comments_router.get(path='/get_all', response_model=dict)
def get_all_comments() -> dict:
    return comments.get_all_comments()
