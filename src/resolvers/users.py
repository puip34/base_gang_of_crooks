from server.database.db_manager import db_manager
from server.database.models import User

def create_user(username: str, email: str) -> dict:
    res = db_manager.execute(query="INSERT INTO users (username, email) VALUES (?, ?) RETURNING id, username, email", args=(username, email))
    res["result"] = None if not res["result"] else User(id=res["result"][0], username=res["result"][1], email=res["result"][2])
    return res

def get_all_users() -> dict:
    res = db_manager.execute(query="SELECT * FROM users", many=True)
    list_users = [User(id=item[0], username=item[1], email=item[2]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_users else list_users
    return res
