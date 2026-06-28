# 🚀 FastAPI with JWT Auth serving a LangChain ReAct AI Agent

A production-style AI Agent API built with **FastAPI**, featuring **JWT authentication**, **Groq-powered LLMs**, and a **ReAct-style tool-using agent** with Wikipedia integration.

This project demonstrates how to build a tool-augmented AI system that can:

- 🧠 Reason about user intent
- 🌐 Use external tools when needed
- 💬 Respond directly for conversational and creative tasks

---

## 📌 Project Info

- 📦 Version: 0.0.2
- 🐍 Python: 3.12
- 📅 Last Updated: 28-06-2026

---

## ✨ Features

### 🔐 Authentication (JWT)

- Secure login system using JWT (HS256)
- Protected endpoints with Bearer token
- Token expiration support
- Environment-based credentials (.env)

---

### 🤖 AI Agent (ReAct-style reasoning)

- 🧠 Reasoning + Acting loop
- 🔁 Step-based decision making (router → tool → answer)
- 🎯 Smart tool selection (Wikipedia only when needed)
- 🧯 Robust error handling
- 🪵 Full trace logging of agent steps

---

### 🧠 LLM Integration (Groq)

- ⚡ Model: openai/gpt-oss-20b
- 🚀 High-speed inference via Groq API
- 🎛️ Deterministic outputs (temperature = 0)

---

### 🌐 Wikipedia Tool

- 📚 Wikipedia REST API integration
- 🔎 Direct page lookup + search fallback
- 📊 Simple relevance scoring for best match selection
- 🧯 Graceful error handling and safe fallbacks

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
| 🔐 POST | /login | Get JWT token |
| 💬 POST | /chat | Chat with AI agent (protected) |
| ❤️ GET | /health | Service health check |
| 🧠 GET | /test-groq | Test LLM connection |
| 🌐 GET | /test-wikipedia | Test Wikipedia tool |

---

## ⚙️ Getting Started

### 1️⃣ Clone Repository

Clone the project and enter the directory.

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

python -c import secrets; print(secrets.token_hex(32))

---

## ▶️ Run the Application

uvicorn main:app --reload

App:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Call /login
2. Receive JWT token
3. Use token in requests:

Authorization: Bearer YOUR_TOKEN

---

## 🧠 How the Agent Works

User Input
↓
Router decides: wikipedia or none
↓
If needed → Wikipedia tool
↓
Otherwise → direct LLM response
↓
Final answer generation

---

## 🏗️ Architecture

LLM:
Groq - openai/gpt-oss-20b

Agent:
Custom ReAct-style loop (router + tool execution + final answer)

Tools:
Wikipedia REST API

Execution Settings:
- Max tool usage: 1 per request
- Temperature: 0
- Structured trace logging enabled

---

## 🌐 Wikipedia Tool Flow

1. Try direct page lookup
2. If not found → search API
3. Score candidates based on keyword overlap
4. Fetch best matching summary

---

## 💬 Example Requests

### 😂 Joke Request

{
  "message": "Tell me a joke"
}

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Sure! Here’s a quick one:\n\n**Why don’t scientists trust atoms?**\n\nBecause they make up everything!"
  }
}

---

### 🌐 Factual Question using Wikipedia Tool

{
  "message": "What is the capital of France?"
}

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Wikipedia",
    "action_input": "What is the capital of France?",
    "observation": "A capital city, or just capital, is the municipality holding primary status in a country, state, province, department, or other subnational division, usually as its seat of government. A capital is typically a city that physically encompasses the government's offices and meeting places; the status as capital is often designated by law or a constitution. In some jurisdictions, including several countries, different branches of government are in different settlements, sometimes meaning there are multiple official capitals. In some cases, a distinction is made between the official (constitutional) capital and the seat of government.",
    "final_answer": "The capital of France is **Paris**."
  }
}

---

### ✍️ Creative Request

{
  "message": "Write me a short poem"
}

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Beneath the quiet moon’s soft glow,  \nI hear the wind in whispers low,  \nIts song a thread of silver light,  \nWeaving dreams through the night."
  }
}

---

## 📌 Use Cases

- 🤖 AI assistants
- 🎓 Educational tools
- 🧪 LangChain-style agent experimentation
- 🧠 Tool-augmented LLM systems
- ⚡ FastAPI AI backends

---

## 🚧 Limitations

- 📚 Only Wikipedia as external tool
- 🧠 No long-term memory
- 🔐 Demo authentication system
- 🌐 Limited external knowledge sources

---

## 🚀 Future Improvements

- 🧠 Conversation memory
- 🔌 Additional tools (search, databases, APIs)
- 👥 Multi-user system
- 🔄 Token refresh mechanism
- 📊 Observability dashboard

---

## 📄 License

MIT License

---

## 🙌 Summary

This project combines:

⚡ FastAPI  
🔐 JWT Authentication  
🧠 Groq LLM (openai/gpt-oss-20b)  
🤖 ReAct-style AI Agent  
🌐 Wikipedia Tool  

into a lightweight but extensible tool-augmented AI system capable of reasoning, acting, and responding dynamically based on user intent.