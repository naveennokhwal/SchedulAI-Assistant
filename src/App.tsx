import React, { useState, useEffect, useRef } from 'react';
import { Header } from './components/Header';
import { ChatMessage } from './components/ChatMessage';
import { ChatInput } from './components/ChatInput';
import { DataTable } from './components/DataTable';
import { Message } from './types';

const apiUrl = import.meta.env.VITE_BACKEND_URL;
console.log("API URL:", apiUrl);

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isInitialLoading, setIsInitialLoading] = useState(true);
  const [tableData, setTableData] = useState<[string, string, string, string][]>([]);
  const [tableType, setTableType] = useState<'tasks' | 'alarms' | 'reminders' | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    fetchInitialMessage();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const fetchInitialMessage = async () => {
    try {
      const response = await fetch(`${apiUrl}/chat/history`);
      const data = await response.json();
      setMessages(data);
    } catch (error) {
      console.error('Failed to load initial message:', error);
      setMessages([{
        id: 'welcome',
        content: "Hello! I'm your AI assistant. How can I help you today?",
        role: 'assistant',
        timestamp: new Date().toISOString()
      }]);
    } finally {
      setIsInitialLoading(false);
    }
  };

  const fetchData = async (type: 'tasks' | 'alarms' | 'reminders') => {
    try {
      if (tableType === type) {
        // If clicking the same button, hide the table
        setTableType(null);
        setTableData([]);
        return;
      }

      const response = await fetch(`${apiUrl}/${type}`);
      const data = await response.json();
      setTableData(data);
      setTableType(type);
    } catch (error) {
      console.error(`Failed to fetch ${type}:`, error);
    }
  };

  const handleSendMessage = async (content: string) => {
    const newMessage: Message = {
      id: Date.now().toString(),
      content,
      role: 'user',
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, newMessage]);
    setIsLoading(true);

    try {
      const response = await fetch(`${apiUrl}/chat/message`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: content }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response from assistant');
      }

      const data = await response.json();
      
      const assistantMessage: Message = {
        id: Date.now().toString(),
        content: data.response,
        role: 'assistant',
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Failed to send message:', error);
      const errorMessage: Message = {
        id: Date.now().toString(),
        content: "I'm sorry, I'm having trouble responding right now. Please try again later.",
        role: 'assistant',
        timestamp: new Date().toISOString(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleStartVoiceInput = () => {
    console.log('Voice input started');
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900">
      <Header
        onTasksClick={() => fetchData('tasks')}
        onAlarmsClick={() => fetchData('alarms')}
        onRemindersClick={() => fetchData('reminders')}
      />
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {tableType && tableData.length > 0 && (
          <DataTable data={tableData} type={tableType} />
        )}
        {isInitialLoading ? (
          <div className="text-gray-400 animate-pulse">Loading chat history...</div>
        ) : (
          <>
            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
            ))}
            {isLoading && (
              <div className="text-gray-400 animate-pulse">Assistant is typing...</div>
            )}
            <div ref={messagesEndRef} />
          </>
        )}
      </div>
      <ChatInput
        onSendMessage={handleSendMessage}
        onStartVoiceInput={handleStartVoiceInput}
      />
    </div>
  );
}

export default App;