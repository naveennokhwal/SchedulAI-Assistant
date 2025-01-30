import sqlite3
from datetime import datetime, timedelta

class DB:
    def __init__(self):
        # Initialize SQLite database to store alarms
        self.conn = sqlite3.connect('tasks.db', check_same_thread= False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create tasks table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                label TEXT NOT NULL,
                                date TEXT NOT NULL,
                                time TEXT NOT NULL,
                                status INTEGER NOT NULL,
                                class_type TEXT NOT NULL)''')
        self.conn.commit()


    def add_task(self, label, date, time, class_type, status = 0):
        # Set a new alarm (add to database)
        self.cursor.execute("INSERT INTO tasks (label, date, time, status, class_type) VALUES (?, ?, ?, ?, ?)", 
                            (label, date, time, status, class_type))
        self.conn.commit()

        if self.is_exist(label, date, time, class_type):
            return True
        else: 
            return False

    def edit_task(self, old_label, old_date, old_time, new_label, new_date, new_time, class_type ):
        # Edit an existing alarm
        self.cursor.execute("UPDATE tasks SET label = ?, date = ?, time = ? WHERE label = ? AND date = ? AND time = ? AND class_type = ?",
                            (new_label, new_date, new_time, old_label, old_date, old_time, class_type))
        self.conn.commit()

        if self.is_exist(new_label, new_date, new_time, class_type):
            return True
        else:
            return False

    def is_exist(self, label, date, time, class_type):
        self.cursor.execute("SELECT * FROM tasks WHERE label = ? AND date = ? AND time = ? AND class_type = ?", 
                            (label, date, time, class_type))
        task = self.cursor.fetchall()
        self.conn.commit()
        if task:
            return True
        else:
            return False
        
    def delete_task(self, label, date, time, class_type):
        # Delete a specific alarm from the database
        self.cursor.execute("DELETE FROM tasks WHERE label = ? AND date = ? AND time = ? AND class_type = ?", 
                            (label, date, time, class_type))
        self.conn.commit()

        if self.is_exist(label, date, time, class_type):
            return False
        else:
            return True

    def search_label(self, label, class_type):
        self.cursor.execute("SELECT label, date, time FROM tasks WHERE label = ? AND class_type = ?", (label, class_type))  # Select specific columns
        task = self.cursor.fetchone()  # Fetch one row
        if task:
            return task  # Convert the tuple to a list
        else: 
            return None

    def show_tasks(self, class_type):
        # Show all tasks based on the given class_type
        self.cursor.execute("SELECT label, date, time, status FROM tasks WHERE class_type = ?", (class_type,))
        tasks = self.cursor.fetchall()
        if tasks:
            return list(tasks)  # Returns a list of tuples containing the rows
        else:
            return None  # Explicitly return an empty list if no tasks match        
    
    def __del__(self):
        self.conn.close()

