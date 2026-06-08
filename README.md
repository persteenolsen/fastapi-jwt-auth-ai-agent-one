# 🚀 Python + FastAPI + JWT Auth + AI Agent + Groq + LangChain

A production-style AI Agent API built with **FastAPI**, featuring **JWT authentication**, **Groq-powered LLMs**, and a **LangChain ReAct agent** with tool usage (Wikipedia).

This project demonstrates how to build a tool-using AI system that can:
- 🧠 Reason about user intent
- 🌐 Use external tools when needed
- 💬 Respond directly for conversational and creative tasks

---

## 📌 Project Info

- 📦 Version: 0.0.2
- 🐍 Python: 3.12
- 📅 Last Updated: 08-06-2026

---

## ✨ Features

### 🔐 Authentication (JWT)
- Secure login system using JWT (HS256)
- Protected endpoints with Bearer token
- Token expiration support
- Environment-based credentials (.env)

---

### 🤖 AI Agent (LangChain ReAct)

- 🧠 Reasoning + Acting loop (ReAct pattern)
- 🔁 Multi-step decision making
- 🎯 Smart tool selection (Wikipedia only when needed)
- 🛑 Controlled iterations (prevents infinite loops)
- 🧯 Parsing error handling for stability

---

### 🧠 LLM Integration (Groq)

- ⚡ Model: `llama-3.3-70b-versatile`
- 🚀 Ultra-fast inference via Groq API
- 🎛️ Deterministic outputs (`temperature = 0`)

---

### 🌐 Wikipedia Tool

- 📚 Wikipedia API integration via custom wrapper
- 🔎 Factual knowledge retrieval
- 🔁 Retry support for transient API failures
- 🧯 Graceful fallback on errors
- 🧠 Used only for factual queries

---

### 🧩 Agent Capabilities

- ❓ General question answering
- 📚 Factual lookup (Wikipedia)
- 💬 Conversational chat
- 😂 Joke generation
- ✍️ Creative writing (poems, stories)
- 🧠 Tool-augmented reasoning

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| 🔐 POST | `/login` | Get JWT token |
| 💬 POST | `/chat` | Chat with AI agent (protected) |
| ❤️ GET | `/health` | Service health check |
| 🧠 GET | `/test-groq` | Test LLM connection |
| 🌐 GET | `/test-wikipedia` | Test Wikipedia tool |

---

## ⚙️ Getting Started

### 1️⃣ Clone Repository

Clone the project from GitHub and enter the project directory.

---

### 2️⃣ Create Virtual Environment

Windows:
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file:

SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key
FAKE_USERNAME=admin
FAKE_PASSWORD=password

Generate a secure key:

python -c "import secrets; print(secrets.token_hex(32))"

---

## ▶️ Run the Application

uvicorn main:app --reload

App:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Call `/login`
2. Receive JWT token
3. Use token in requests:

Authorization: Bearer YOUR_TOKEN

---

## 🧠 How the Agent Works

User Input
↓
Agent Reasoning
↓
Wikipedia Tool (if needed)
↓
Direct Response (jokes, chat, creative writing)
↓
Final Answer

---

## 🏗️ Architecture

LLM:
Groq - llama-3.3-70b-versatile

Agent:
LangChain ReAct Agent

Tools:
Wikipedia API

Execution Settings:
Max iterations: 2
Parsing error handling enabled
Verbose logging enabled

---

## 💬 Example Requests

### 😂 Joke Request

{
  "message": "Tell me a joke"
}

Response:

{
  "response": "Here's one: Why couldn't the bicycle stand up by itself? Because it was two-tired."
}

---

### 📚 Factual Question

{
  "message": "What is the capital of France?"
}

Response:

{
  "response": "Paris"
}

---

### ✍️ Creative Request

{
  "message": "Write a short poem"
}

Response:

{
  "response": "The sun sets slow and paints the sky..."
}

---

### 🌐 Wikipedia Tool Usage

{
  "message": "Who is Albert Einstein?"
}

Response:

{
  "response": "Albert Einstein was a theoretical physicist known for the theory of relativity."
}

---

## 📌 Use Cases

- 🤖 AI assistants
- 🎓 Educational tools
- 🧪 LangChain experimentation
- 🧠 Tool-augmented LLM systems
- ⚡ FastAPI backend AI services

---

## 🚧 Limitations

- 📚 Only Wikipedia as external tool
- 🧠 No long-term memory
- 🔐 Demo authentication system
- 🌐 Limited external knowledge sources

---

## 🚀 Future Improvements

- 🧠 Conversation memory
- 🔌 More tools (search, APIs, DB integration)
- 👥 Multi-user system
- 🔄 Token refresh system
- 🧩 Modular tool registry
- 📊 Analytics dashboard

---

## 📄 License

MIT License

---

## 🙌 Summary

This project combines:

⚡ FastAPI  
🔐 JWT Authentication  
🧠 Groq LLM (Llama 3.3 70B)  
🤖 LangChain ReAct Agent  
🌐 Wikipedia Tool  

to build a **working tool-augmented AI system** that can reason, act, and respond intelligently depending on user intent.