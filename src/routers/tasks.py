import fastapi
from sqlalchemy.orm import Session
from server.database import db_manager
from server.database.schemas import Task, TaskCreate
from server.resolvers import tasks

tasks_router = fastapi.APIRouter(prefix='/tasks', tags=["Tasks"])

@tasks_router.post("/", response_model=Task)
async def create_task(task: TaskCreate, db: Session = fastapi.Depends(db_manager.get_db)):
    return tasks.create_task(db, task)

@tasks_router.get("/{task_id}", response_model=Task)
async def read_task(task_id: int, db: Session = fastapi.Depends(db_manager.get_db)):
    return tasks.get_task(db, task_id)

@tasks_router.get("/", response_model=list[Task])
async def read_tasks(skip: int = 0, limit: int = 10, db: Session = fastapi.Depends(db_manager.get_db)):
    return tasks.get_all_tasks(db, skip=skip, limit=limit)

@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate, db: Session = fastapi.Depends(db_manager.get_db)):
    return tasks.update_task(db, task_id, task)

@tasks_router.delete("/{task_id}", response_model=None)
async def delete_task(task_id: int, db: Session = fastapi.Depends(db_manager.get_db)):
    return tasks.delete_task(db, task_id)
