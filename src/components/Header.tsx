import React from 'react';
import { AlarmClock, Calendar, ListTodo } from 'lucide-react';

interface HeaderProps {
  onTasksClick: () => void;
  onAlarmsClick: () => void;
  onRemindersClick: () => void;
}

export function Header({ onTasksClick, onAlarmsClick, onRemindersClick }: HeaderProps) {
  return (
    <header className="bg-gray-800 p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold text-white">AI Assistant</h1>
      <div className="flex gap-4">
        <button
          onClick={onTasksClick}
          className="p-2 hover:bg-gray-700 rounded-full transition-colors"
          title="Tasks"
        >
          <ListTodo className="h-6 w-6 text-blue-400" />
        </button>
        <button
          onClick={onAlarmsClick}
          className="p-2 hover:bg-gray-700 rounded-full transition-colors"
          title="Alarms"
        >
          <AlarmClock className="h-6 w-6 text-green-400" />
        </button>
        <button
          onClick={onRemindersClick}
          className="p-2 hover:bg-gray-700 rounded-full transition-colors"
          title="Reminders"
        >
          <Calendar className="h-6 w-6 text-purple-400" />
        </button>
      </div>
    </header>
  );
}