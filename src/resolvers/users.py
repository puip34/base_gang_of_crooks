from server.database.db_manager import db_manager
from server.database.models import User

def create_user(username: str, password: str, email: str, role: str) -> dict:
    res = db_manager.execute(
        query="INSERT INTO Users (Username, Password, Email, Role) VALUES (?, ?, ?, ?) RETURNING UserID, Username, Role",
        args=(username, password, email, role)
    )
    res["result"] = None if not res["result"] else User(id=res["result"][0], username=res["result"][1], role=res["result"][2])
    return res

def get_all_users() -> dict:
    res = db_manager.execute(query="SELECT * FROM Users", many=True)
    list_users = [User(id=item[0], username=item[1], role=item[4]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_users else list_users
    return res
