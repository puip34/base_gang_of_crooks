# task_manager_app/src/start_server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from task_manager_app.src.server.routers import users, projects, tasks, comments
from task_manager_app.src.database.db_manager import create_tables

app = FastAPI()

# Allow all origins during development (CORS setup)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.users_router)
app.include_router(projects.projects_router)
app.include_router(tasks.tasks_router)
app.include_router(comments.comments_router)

# Database setup
create_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
