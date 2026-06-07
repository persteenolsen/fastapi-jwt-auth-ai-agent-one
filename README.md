# Python + FastAPI + JWT Auth + AI Agent + Groq + LLM + LangChain

A production-style AI Agent API built with FastAPI, featuring JWT authentication, Groq-powered LLMs, and LangChain agent orchestration.

This project demonstrates how to build a tool-using AI agent that can reason, take actions, and fetch real-world information (via Wikipedia) before generating responses.

---

## 📌 Project Info

- Version: 0.0.2  
- Python: 3.12  
- Last Updated 07-06-2026  

---

## ✨ Features

### 🔐 Authentication
- JWT-based authentication (HS256)
- Secure protected endpoints
- Token expiration handling
- Environment-based credentials

---

### 🤖 AI Agent (LangChain)
- ReAct agent (Reasoning + Acting loop)
- Multi-step reasoning with tool usage
- Controlled iteration limits for safety
- Robust parsing error handling

---

### 🧠 LLM Integration (Groq)
- Model: llama-3.3-70b-versatile
- Fast inference via Groq API
- Deterministic responses (temperature = 0)

---

### 🌐 Tool Integration (Wikipedia)
- Safe Wikipedia API wrapper via LangChain
- Top-K search results for better context
- Graceful fallback when API fails
- Automatic fallback to LLM knowledge

---

### 🧩 Agent Capabilities
- Answers general knowledge questions
- Uses Wikipedia when factual lookup is needed
- Combines reasoning + external tools
- Produces structured final answers

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /login | Get JWT token |
| POST | /chat | Chat with AI agent (protected) |
| GET | /health | Service health check |
| GET | /test-groq | Test LLM connection |
| GET | /test-wikipedia | Test Wikipedia tool |

---

## ⚙️ Getting Started

### 1. Clone Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

---

### 2. Create Virtual Environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install Dependencies
pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file:

SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key
FAKE_USERNAME=admin
FAKE_PASSWORD=password

Optional key generation:
python -c import secrets; print(secrets.token_hex(32))

---

## ▶️ Run Application

uvicorn main:app --reload

API: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs  

---

## 🔐 Authentication Flow

1. Call `/login`
2. Receive JWT token
3. Use in request header:

Authorization: Bearer YOUR_TOKEN

---

## 🧠 How the Agent Works

User question  
→ ReAct Agent decides  
→ Tool usage (Wikipedia if needed)  
→ Observation  
→ Loop until solved  
→ Final answer from LLM  

---

## 🧩 Architecture

LLM:
Groq llama-3.3-70b-versatile

Agent Type:
ReAct (Reasoning + Acting)

Tools:
Wikipedia via LangChain API

Execution Control:
Max iterations: 5
Error handling enabled
Verbose logging enabled

---

## 💬 Example Request / Response

POST /chat

Request (Will most likely just use LLM):

{
  "message": "Tell me a joke"
}

Response:

{
  "response": "Why don't scientists trust atoms? Because they make up everything."
}

Request (Will most likely just use LLM):

{
  "message": "What is the capital of France?"
}

Response:

{
  "response": "Paris"
}

Request (Will most likely try to use the Wikipedia Tool):

{
  "message": "What is Python?"
}

Response:

{
  "response": "Python is a high-level, interpreted programming language widely used for web development, scientific computing, and data analysis."
}

---

## 📌 Use Cases

- AI assistants
- Knowledge-based chat systems
- Tool-augmented LLM agents
- Education and demos

---

## 🚧 Limitations

- Only Wikipedia as external tool
- No memory (stateless)
- Demo authentication only

---

## 🚀 Future Improvements

- Add memory (conversation history)
- Add more tools (search, APIs)
- Multi-user authentication
- Token refresh system
- Modular project structure

---

## 📄 License

MIT License

---

## 🙌 Final Notes

This project combines FastAPI, JWT authentication, Groq LLMs, and LangChain agents into a working tool-using AI system.