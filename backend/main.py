from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

from backend.agent.agent import Agent
from backend.services.show import Show
app = FastAPI()
show = Show()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Message model
class Message(BaseModel):
    id: str
    content: str
    role: str
    timestamp: str

class MessageRequest(BaseModel):
    message: str

# In-memory storage for chat history
chat_history: List[Message] = []

@app.get("/chat/history")
async def get_chat_history():
    # Return a welcome message for new sessions
    return [{
        "id": str(uuid.uuid4()),
        "content": "Hello! I'm your AI assistant. How can I help you today?",
        "role": "assistant",
        "timestamp": datetime.now().isoformat()
    }]

@app.get("/tasks")
async def get_tasks():
    return show.show_tasks()

@app.get("/alarms")
async def get_alarms():
    return show.show_alarms()

@app.get("/reminders")
async def get_reminders():
    return show.show_reminders()

@app.post("/chat/message")
async def send_message(message_request: MessageRequest):
    # Create user message
    user_message = Message(
        id=str(uuid.uuid4()),
        content=message_request.message,
        role="user",
        timestamp=datetime.now().isoformat()
    )
    chat_history.append(user_message)
    
    agent = Agent(message_request.message)
    response_content = agent.decide()
    
    # Create assistant message
    assistant_message = Message(
        id=str(uuid.uuid4()),
        content=response_content,
        role="assistant",
        timestamp=datetime.now().isoformat()
    )
    chat_history.append(assistant_message)
    
    return {"response": response_content}
