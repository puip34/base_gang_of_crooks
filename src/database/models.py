from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from .db_manager import Base

class User(Base):
    __tablename__ = "users"

    UserID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(255), unique=True, index=True)
    Password = Column(String(255))
    Email = Column(String(255))
    Role = Column(String(50))

    roles = relationship("UserRole", back_populates="user")

class Role(Base):
    __tablename__ = "roles"

    RoleID = Column(Integer, primary_key=True, index=True)
    RoleName = Column(String(50), index=True)

    user_roles = relationship("UserRole", back_populates="role")
    project_user_roles = relationship("ProjectUserRole", back_populates="role")

class Project(Base):
    __tablename__ = "projects"

    ProjectID = Column(Integer, primary_key=True, index=True)
    ProjectName = Column(String(255), index=True)
    Description = Column(Text)
    CreatorUserID = Column(Integer, ForeignKey("users.UserID"))

    creator_user = relationship("User", back_populates="roles")
    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = "tasks"

    TaskID = Column(Integer, primary_key=True, index=True)
    TaskName = Column(String(255), index=True)
    Description = Column(Text)
    ProjectID = Column(Integer, ForeignKey("projects.ProjectID"))
    CreatorUserID = Column(Integer, ForeignKey("users.UserID"))
    AssigneeUserID = Column(Integer, ForeignKey("users.UserID"))

    project = relationship("Project", back_populates="tasks")
    creator_user = relationship("User", back_populates="roles")
    assignee_user = relationship("User", back_populates="roles")

class Comment(Base):
    __tablename__ = "comments"

    CommentID = Column(Integer, primary_key=True, index=True)
    TaskID = Column(Integer, ForeignKey("tasks.TaskID"))
    UserID = Column(Integer, ForeignKey("users.UserID"))
    CommentText = Column(Text)
    Timestamp = Column(TIMESTAMP)

    task = relationship("Task", back_populates="comments")
    user = relationship("User", back_populates="roles")

class UserRole(Base):
    __tablename__ = "user_roles"

    UserRolesID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))
    RoleID = Column(Integer, ForeignKey("roles.RoleID"))

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="user_roles")

class ProjectUserRole(Base):
    __tablename__ = "project_user_roles"

    ProjectUserRolesID = Column(Integer, primary_key=True, index=True)
    ProjectID = Column(Integer, ForeignKey("projects.ProjectID"))
    UserID = Column(Integer, ForeignKey("users.UserID"))
    RoleID = Column(Integer, ForeignKey("roles.RoleID"))

    project = relationship("Project", back_populates="project_user_roles")
    user = relationship("User", back_populates="project_user_roles")
    role = relationship("Role", back_populates="project_user_roles")

class CompletedProject(Base):
    __tablename__ = "completed_projects"

    CompletedProjectID = Column(Integer, primary_key=True, index=True)
    ProjectID = Column(Integer, ForeignKey("projects.ProjectID"))
    CompletionDate = Column(Date)

    project = relationship("Project", back_populates="completed_projects")

class TaskStatus(Base):
    __tablename__ = "task_status"

    TaskStatusID = Column(Integer, primary_key=True, index=True)
    StatusName = Column(String(50), index=True)

    tasks = relationship("Task", back_populates="status")

class TaskHistory(Base):
    __tablename__ = "task_history"

    TaskHistoryID = Column(Integer, primary_key=True, index=True)
    TaskID = Column(Integer, ForeignKey("tasks.TaskID"))
    StatusID = Column(Integer, ForeignKey("task_status.TaskStatusID"))
    Timestamp = Column(TIMESTAMP)

    task = relationship("Task", back_populates="history")
    status = relationship("TaskStatus", back_populates="tasks")
