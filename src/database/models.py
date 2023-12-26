from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str
    email: str
    role: str

class Role(BaseModel):
    id: int
    name: str

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str]
    creator_user_id: int

class Task(BaseModel):
    id: int
    name: str
    description: Optional[str]
    project_id: int
    creator_user_id: int
    assignee_user_id: Optional[int]

class Comment(BaseModel):
    id: int
    task_id: int
    user_id: int
    comment_text: str
    timestamp: Optional[str]

class UserRole(BaseModel):
    id: int
    user_id: int
    role_id: int

class ProjectUserRole(BaseModel):
    id: int
    project_id: int
    user_id: int
    role_id: int

class CompletedProject(BaseModel):
    id: int
    project_id: int
    completion_date: Optional[str]

class TaskStatus(BaseModel):
    id: int
    status_name: str

class TaskHistory(BaseModel):
    id: int
    task_id: int
    status_id: int
    timestamp: Optional[str]
