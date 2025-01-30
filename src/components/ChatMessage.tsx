import React from 'react';
import { Message } from '../types';
import { Bot, User } from 'lucide-react';

interface ChatMessageProps {
  message: Message;
}

export function ChatMessage({ message }: ChatMessageProps) {
  const isAssistant = message.role === 'assistant';
  
  return (
    <div className={`flex ${isAssistant ? 'justify-start' : 'justify-end'} gap-3`}>
      <div className={`flex gap-3 max-w-[80%] ${isAssistant ? 'bg-gray-800' : 'bg-blue-600'} p-4 rounded-lg`}>
        {isAssistant && (
          <div className="flex-shrink-0">
            <Bot className="h-6 w-6 text-blue-400" />
          </div>
        )}
        <div className="flex-1">
          <p className="text-gray-100">{message.content}</p>
          <span className="text-xs text-gray-400 mt-1">
            {new Date(message.timestamp).toLocaleTimeString()}
          </span>
        </div>
        {!isAssistant && (
          <div className="flex-shrink-0">
            <User className="h-6 w-6 text-blue-200" />
          </div>
        )}
      </div>
    </div>
  );
}