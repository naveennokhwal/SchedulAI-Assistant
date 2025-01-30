import React, { useState } from 'react';
import { Mic, Send } from 'lucide-react';

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  onStartVoiceInput: () => void;
}

export function ChatInput({ onSendMessage, onStartVoiceInput }: ChatInputProps) {
  const [message, setMessage] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 p-4 bg-gray-800">
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
        className="flex-1 bg-gray-700 text-white rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        type="button"
        onClick={onStartVoiceInput}
        className="p-2 bg-gray-700 text-gray-300 rounded-lg hover:bg-gray-600 transition-colors"
      >
        <Mic className="h-5 w-5" />
      </button>
      <button
        type="submit"
        className="p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        <Send className="h-5 w-5" />
      </button>
    </form>
  );
}