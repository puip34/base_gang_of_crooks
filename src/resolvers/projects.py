from server.database.db_manager import db_manager
from server.database.models import Project

def create_project(project_name: str, description: str, creator_user_id: int) -> dict:
    res = db_manager.execute(
        query="INSERT INTO Projects (ProjectName, Description, CreatorUserID) VALUES (?, ?, ?) RETURNING ProjectID, ProjectName",
        args=(project_name, description, creator_user_id)
    )
    res["result"] = None if not res["result"] else Project(id=res["result"][0], name=res["result"][1])
    return res

def get_all_projects() -> dict:
    res = db_manager.execute(query="SELECT * FROM Projects", many=True)
    list_projects = [Project(id=item[0], name=item[1]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_projects else list_projects
    return res
