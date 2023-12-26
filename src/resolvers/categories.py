from server.database.db_manager import db_manager
from server.database.models import Category

def create_category(category_name: str) -> dict:
    res = db_manager.execute(query="INSERT INTO categories (name) VALUES (?) RETURNING id, name", args=(category_name,))
    res["result"] = None if not res["result"] else Category(id=res["result"][0], name=res["result"][1])
    return res

def get_all_categories() -> dict:
    res = db_manager.execute(query="SELECT * FROM categories", many=True)
    list_categories = [Category(id=item[0], name=item[1]) for item in res["result"]] if res["result"] else []
    res["result"] = None if not list_categories else list_categories
    return res
