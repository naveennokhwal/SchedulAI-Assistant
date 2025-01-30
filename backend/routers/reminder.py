
from datetime import datetime
from backend.services.database import DB

class ReminderManager:
    def __init__(self):
        self.db = DB()
    
    def set_reminder(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Reminder. Please try again with defined label."
        
        elif date == None:
            return f"For what date you want to set this reminder? Please try again with specified date."
        elif time == None:
            return f"For what time you want to set this reminder? Please try again with specified time."

        is_exist = self.db.search_label(label, "REMINDER")
        if is_exist:
            return f"There already exist a reminder with the same label."
        else:
            is_reminder_set = self.db.add_task(label, date, time, "REMINDER")
            if is_reminder_set:
                return f"Reminder is set for {label} on {date} at {time}."
            else: 
                return f"Due to some internal problem your reminder is not set, please try again."

    def edit_reminder(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Reminder. Please try again with defined label."
        
        existing_reminder = self.db.search_label(label, "REMINDER")
        if existing_reminder == None:
            return f"There is no reminder with the label: {label}"
        
        if date == None and time == None:
            return f"Please specify date or time that you want to edit in exising reminder?"
        
        is_date_edit = False
        is_time_edit = False
        if date != None:
            is_date_edit = self.db.edit_task(existing_reminder[0], existing_reminder[1], existing_reminder[2], label, date, existing_reminder[2], "REMINDER")

        if time != None:
            is_time_edit = self.db.edit_task(existing_reminder[0], existing_reminder[1], existing_reminder[2], label, existing_reminder[1], date, "REMINDER")

        if is_date_edit or is_time_edit:
            return f"your reminder '{label}' is changed."
        else:
            return f"Due to some internal error your reminder is not edited. please try again."



    def delete_reminder(self, label):
        if label == None:
            return f"You have not specified label of the Reminder. Please try again with defined label."
        
        existing_reminder = self.db.search_label(label, "REMINDER")

        if existing_reminder == None:
            return f"There is no reminder with the label: {label}"
        
        
        is_deleted = self.db.delete_task(existing_reminder[0], existing_reminder[1], existing_reminder[2], "REMINDER")

        if is_deleted:
            return f"Reminder '{label}' is deleted."
        else:
            return f"Due to some internal error your reminder is not deleted. please try again."

