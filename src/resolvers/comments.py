from server.database.db_manager import db_manager
from server.database.models import Comment

def create_comment(task_id: int, user_id: int, comment_text: str) -> dict:
    res = db_manager.execute(
        query="INSERT INTO Comments (TaskID, UserID, CommentText) VALUES (?, ?, ?) RETURNING CommentID, CommentText",
        args=(task_id, user_id, comment_text)
    )
    res["result"] = None if not res["result"] else Comment(id=res["result"][0], text=res["result"][1])
    return res

def get_all_comments() -> dict:
    res = db_manager.execute(query="SELECT * FROM Comments", many=True)
    list_comments = [Comment(id=item[0], text=item[1]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_comments else list_comments
    return res
