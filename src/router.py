from fastapi import APIRouter
from .routers import (
    users_router,
    roles_router,
    projects_router,
    tasks_router,
    comments_router,
)

router = APIRouter()

router.include_router(users_router)
router.include_router(roles_router)
router.include_router(projects_router)
router.include_router(tasks_router)
router.include_router(comments_router)
