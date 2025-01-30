export interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: string;
}

export interface Task {
  id: string;
  title: string;
  dueDate: string;
  completed: boolean;
}

export interface Alarm {
  id: string;
  time: string;
  active: boolean;
}

export interface Reminder {
  id: string;
  text: string;
  dateTime: string;
  completed: boolean;
}