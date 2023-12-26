from server.database.db_manager import db_manager
from server.database.models import Task

def create_task(task_name: str, description: str, project_id: int, creator_user_id: int, assignee_user_id: int) -> dict:
    res = db_manager.execute(
        query="INSERT INTO Tasks (TaskName, Description, ProjectID, CreatorUserID, AssigneeUserID) VALUES (?, ?, ?, ?, ?) RETURNING TaskID, TaskName",
        args=(task_name, description, project_id, creator_user_id, assignee_user_id)
    )
    res["result"] = None if not res["result"] else Task(id=res["result"][0], name=res["result"][1])
    return res

def get_all_tasks() -> dict:
    res = db_manager.execute(query="SELECT * FROM Tasks", many=True)
    list_tasks = [Task(id=item[0], name=item[1]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_tasks else list_tasks
    return res
