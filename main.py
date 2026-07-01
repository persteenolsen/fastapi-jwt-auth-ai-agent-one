from fastapi import FastAPI
from routes import router
from config import logger

app = FastAPI(
    title="FastAPI with JWT Auth serving a ReAct-inspired AI agent system using LangChain",
    description="01-07-2026 - FastAPI with JWT authentication serving a ReAct-inspired LLM system using LangChain and Groq, with optional Wikipedia tool access",
    version="0.0.3", 
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

# Include API routes
app.include_router(router)