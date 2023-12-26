from sqlalchemy.orm import Session
from typing import List

from server.database.models import Task as DBTask
from server.database.schemas import Task as TaskModel

def create_task(db: Session, task: TaskModel) -> TaskModel:
    db_task = DBTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int) -> DBTask:
    return db.query(DBTask).filter(DBTask.id == task_id).first()

def get_all_tasks(db: Session) -> List[DBTask]:
    return db.query(DBTask).all()

def update_task(db: Session, task_id: int, updated_task: TaskModel) -> DBTask:
    db_task = get_task(db=db, task_id=task_id)
    for key, value in updated_task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> None:
    db.query(DBTask).filter(DBTask.id == task_id).delete()
    db.commit()