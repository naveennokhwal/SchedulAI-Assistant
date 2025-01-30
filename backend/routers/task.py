from backend.services.database import DB

class TaskManager:
    def __init__(self):
        self.db = DB()
    
    def set_task(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Task. Please try again with defined label."
        
        elif date == None:
            return f"For what date you want to set this task? Please try again with specified date."
        elif time == None:
            return f"For what time you want to set this task? Please try again with specified time."

        is_exist = self.db.search_label(label, "TASK")
        if is_exist:
            return f"There already exist a task with the same label."
        else:
            is_task_set = self.db.add_task(label, date, time, "TASK")
            if is_task_set:
                return f"Task is set for {label} on {date} at {time}."
            else: 
                return f"Due to some internal problem your task is not set, please try again."

    def edit_task(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Task. Please try again with defined label."
        
        existing_task = self.db.search_label(label, "TASK")
        if existing_task == None:
            return f"There is no task with the label: {label}"
        
        if date == None and time == None:
            return f"Please specify date or time that you want to edit in exising task?"
        
        is_date_edit = False
        is_time_edit = False
        if date != None:
            is_date_edit = self.db.edit_task(existing_task[0], existing_task[1], existing_task[2], label, date, existing_task[2], "TASK")

        if time != None:
            is_time_edit = self.db.edit_task(existing_task[0], existing_task[1], existing_task[2], label, existing_task[1], date, "TASK")

        if is_date_edit or is_time_edit:
            return f"your task '{label}' is changed."
        else:
            return f"Due to some internal error your task is not edited. please try again."

    def delete_task(self, label):
        if label == None:
            return f"You have not specified label of the Task. Please try again with defined label."
        
        existing_task = self.db.search_label(label, "TASK")

        if existing_task == None:
            return f"There is no task with the label: {label}"
        
        
        is_deleted = self.db.delete_task(existing_task[0], existing_task[1], existing_task[2], "TASK")

        if is_deleted:
            return f"Task '{label}' is deleted."
        else:
            return f"Due to some internal error your task is not deleted. please try again."