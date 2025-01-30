from backend.services.database import DB

class AlarmManager:
    def __init__(self):
        self.db = DB()
    
    def set_alarm(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Alarm. Please try again with defined label."
        
        elif date == None:
            return f"For what date you want to set this alarm? Please try again with specified date."
        elif time == None:
            return f"For what time you want to set this alarm? Please try again with specified time."

        is_exist = self.db.search_label(label, "ALARM")
        if is_exist:
            return f"There already exist a alarm with the same label."
        else:
            is_alarm_set = self.db.add_task(label, date, time, "ALARM")
            if is_alarm_set:
                return f"Alarm is set for {label} on {date} at {time}."
            else: 
                return f"Due to some internal problem your alarm is not set, please try again."

    def edit_alarm(self, label, date, time):
        if label == None:
            return f"You have not specified label of the Alarm. Please try again with defined label."
        
        existing_alarm = self.db.search_label(label, "ALARM")
        if existing_alarm == None:
            return f"There is no alarm with the label: {label}"
        
        if date == None and time == None:
            return f"Please specify date or time that you want to edit in exising alarm?"
        
        is_edited = self.db.edit_task(existing_alarm[0], existing_alarm[1], existing_alarm[2], label, date, time, "ALARM")

        if is_edited:
            return f"your alarm '{label}' is changed."
        else:
            return f"Due to some internal error your alarm is not edited. please try again."


    def delete_alarm(self, label):
        if label == None:
            return f"You have not specified label of the Alarm. Please try again with defined label."
        
        existing_alarm = self.db.search_label(label, "ALARM")

        if existing_alarm == None:
            return f"There is no alarm with the label: {label}"
        
        
        is_deleted = self.db.delete_task(existing_alarm[0], existing_alarm[1], existing_alarm[2], "ALARM")

        if is_deleted:
            return f"Alarm '{label}' is deleted."
        else:
            return f"Due to some internal error your alarm is not deleted. please try again."
        