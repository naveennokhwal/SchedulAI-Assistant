from typing import List, Tuple
from backend.services.database import DB

class Show:
    def __init__(self):
        self.db = DB()    

    def show_tasks(self) -> List[Tuple[str, str, str, str]]:
        tasks = self.db.show_tasks("TASK")
        if tasks:
            return tasks
        else:
            return []

    def show_alarms(self) -> List[Tuple[str, str, str, str]]:
        tasks = self.db.show_tasks("ALARM")
        if tasks:
            return tasks
        else:
            return []

    def show_reminders(self) -> List[Tuple[str, str, str, str]]:
        tasks = self.db.show_tasks("REMINDER")
        if tasks:
            return tasks
        else:
            return []