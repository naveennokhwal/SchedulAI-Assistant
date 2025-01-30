from datetime import datetime, timedelta
from dateutil import parser

class DateTimeNormalizer:
    def __init__(self, date_input, time_input):
        if date_input != None:
            self.date_input = date_input.lower().strip()
        else:
            self.date_input = date_input
        
        if time_input != None:
            self.time_input = time_input.lower().strip()
        else:
            self.time_input = time_input

        self.entities = []

    def normalize_date(self):
        today = datetime.now().date()
        
        if self.date_input in ["today"]:
            return today.strftime("%Y-%m-%d")
        elif self.date_input in ["tomorrow"]:
            return (today + timedelta(days=1)).strftime("%Y-%m-%d")
        elif self.date_input in ["yesterday"]:
            return (today - timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            try:
                parsed_date = parser.parse(self.date_input, fuzzy=True).date()
                return parsed_date.strftime("%Y-%m-%d")
            except Exception as e:
                raise ValueError(f"Invalid date format: {self.date_input}") from e

    def normalize_time(self):
        if self.time_input in ["morning"]:
            return "08:00:00"
        elif self.time_input in ["noon"]:
            return "12:00:00"
        elif self.time_input in ["evening"]:
            return "18:00:00"
        elif self.time_input in ["night"]:
            return "22:00:00"
        else:
            try:
                parsed_time = parser.parse(self.time_input, fuzzy=True).time()
                return parsed_time.strftime("%H:%M:%S")
            except Exception as e:
                raise ValueError(f"Invalid time format: {self.time_input}") from e

    def get_normalized_datetime(self):
        if self.date_input == None and self.time_input == None:
            self.entities.append(None)
            self.entities.append(None)
        
        elif self.date_input == None and self.time_input != None:
            self.date_input = "today"
            self.entities.append(self.normalize_date())
            self.entities.append(self.normalize_time())

        elif self.date_input != None and self.time_input == None:
            self.date_input == "24:00:00"
            self.entities.append(self.normalize_date())
            self.entities.append(self.normalize_time())

        elif self.date_input != None and self.time_input != None:
            self.entities.append(self.normalize_date())
            self.entities.append(self.normalize_time())
            
        return self.entities
