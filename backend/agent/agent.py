# Import your existing intent classification and entity extraction classes
from backend.models.entity import EntityExtractor
from backend.models.intent import IntentClassifier
from backend.routers.task import TaskManager
from backend.routers.alarm import AlarmManager
from backend.routers.reminder import ReminderManager
from backend.services.format_data import DateTimeNormalizer
from backend.models.greeting import GreetClassifier

reminder = ReminderManager()
alarm = AlarmManager()
task = TaskManager()


class Agent:
    def __init__(self, text):
        self.text = text
        is_greet = GreetClassifier(self.text).is_greeting()
        if is_greet:
            self.intent = "greet"
        else:
            self.intent = IntentClassifier(self.text).result()

    def  decide(self):
        if self.intent == "greet":
            return "Hii! How can I help you today?"
        
        elif self.intent == "add_remainder":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = reminder.set_reminder(entities[0], updated_entities[0], updated_entities[1])
            return response
        
        elif self.intent == "update_remainder":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = reminder.edit_reminder(entities[0], updated_entities[0], updated_entities[1])
            return response

        elif self.intent == "delete_remainder":
            entities = EntityExtractor(self.text).result()
            response = reminder.delete_reminder(entities[0])
            return response

        elif self.intent == "set_alarm":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = alarm.set_alarm(entities[0], updated_entities[0], updated_entities[1])
            return response

        elif self.intent == "edit_alarm":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = alarm.edit_alarm(entities[0], updated_entities[0], updated_entities[1])
            return response

        elif self.intent == "delete_alarm":
            entities = EntityExtractor(self.text).result()
            response = alarm.delete_alarm(entities[0])
            return response

        elif self.intent == "add_task":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = task.set_task(entities[0], updated_entities[0], updated_entities[1])
            return response

        elif self.intent == "update_task":
            entities = EntityExtractor(self.text).result()
            updated_entities = DateTimeNormalizer(entities[1], entities[2]).get_normalized_datetime()
            response = task.edit_task(entities[0], updated_entities[0], updated_entities[1])
            return response

        elif self.intent == "delete_task":
            entities = EntityExtractor(self.text).result()
            response = task.delete_task(entities[0])
            return response

        else:
            return "I am not able to understand!! Please try again..."




    