import fastapi
from server.resolvers import categories

categories_router = fastapi.APIRouter(prefix='/categories', tags=["Categories"])

@categories_router.post(path='/create', response_model=dict)
def create_category(category_name: str) -> dict:
    return categories.create_category(category_name=category_name)

@categories_router.get(path='/get_all', response_model=dict)
def get_all_categories() -> dict:
    return categories.get_all_categories()
