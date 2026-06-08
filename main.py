from fastapi import FastAPI
from routes import router
from config import logger

app = FastAPI(
    title="AI Agent API (Groq + JWT + Safe Wikipedia + ReAct)",
    description="08-06-2026 - Secure AI agent API using FastAPI, JWT auth, Groq LLM, and a safe Wikipedia tool. Designed to prevent infinite loops and ensure reliability on Vercel.",
    version="0.0.3", 
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

# Include API routes
app.include_router(router)