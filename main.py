from fastapi import FastAPI
from routes import router
from config import logger

app = FastAPI(
    title="FastAPI with JWT Auth serving a LangChain ReAct AI Agent",
    description="2026-06-08 - FastAPI with JWT Auth serving a LangChain ReAct AI Agent, built using LangChain and Groq LLM. Includes a Wikipedia tool for factual queries and supports intelligent tool-augmented responses",
    version="0.0.3", 
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

# Include API routes
app.include_router(router)