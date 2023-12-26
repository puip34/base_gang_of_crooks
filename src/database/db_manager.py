import sqlite3
from typing import List, Tuple

class DBManager:
    def __init__(self, db_path: str = "task_manager.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query: str, args: Tuple = None, many: bool = False) -> dict:
        try:
            if args:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)

            if many:
                result = self.cursor.fetchall()
            else:
                result = self.cursor.fetchone()

            self.conn.commit()
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}

# Singleton pattern to ensure a single instance of DBManager
db_manager = DBManager()
