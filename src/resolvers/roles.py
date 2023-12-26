from server.database.db_manager import db_manager
from server.database.models import Role

def create_role(role_name: str) -> dict:
    res = db_manager.execute(query="INSERT INTO Roles (RoleName) VALUES (?) RETURNING RoleID, RoleName", args=(role_name,))
    res["result"] = None if not res["result"] else Role(id=res["result"][0], name=res["result"][1])
    return res

def get_all_roles() -> dict:
    res = db_manager.execute(query="SELECT * FROM Roles", many=True)
    list_roles = [Role(id=item[0], name=item[1]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_roles else list_roles
    return res
