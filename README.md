# 🚀 FastAPI with JWT Authentication serving a LangChain ReAct AI Agent

A FastAPI API featuring JWT authentication and a Groq-powered **LangChain ReAct AI Agent** capable of reasoning about user requests and using external tools when needed.

The agent follows a classic **ReAct (Reason + Act)** workflow, deciding whether to answer directly or retrieve information from Wikipedia before generating a final response.

---

# Version

Local development uses **Python 3.12**.

---

## 📌 Project Info

- Version: 0.0.2
- Python: 3.12
- Architecture: LangChain ReAct Agent
- Last Updated: 01-07-2026

---

## 🎯 Use Cases

This project can serve as the foundation for:

- 🤖 AI assistants
- ⚡ FastAPI AI backends
- 🧠 Tool-augmented LLM systems
- 🧪 LangChain agent experimentation
- 🎓 Educational projects
- 🌐 Knowledge retrieval applications

---

## ✨ Key Features

### 🔐 Authentication

- JWT authentication (HS256)
- Protected `/chat` endpoint
- Token-based authorization
- Environment-based configuration

---

### 🤖 ReAct AI Agent

The agent follows a simple reasoning workflow:

1. **Reason** – The agent decides whether external information is required.
2. **Act** – If needed, the Wikipedia tool retrieves relevant information.
3. **Respond** – The LLM generates the final answer using the retrieved context.

Key properties:

- ReAct-style reasoning loop
- Automatic tool selection
- Direct responses for conversational tasks
- Full trace logging for debugging

---

### 🧠 LLM Integration (Groq)

- Model: `openai/gpt-oss-20b`
- High-speed inference through Groq
- Temperature = 0 for deterministic behavior

Used for:

- Request reasoning
- Tool selection
- Final response generation

---

### 🌐 Wikipedia Tool

The integrated Wikipedia tool provides factual knowledge through:

- Direct page lookup
- Search fallback
- Simple relevance scoring
- Graceful error handling

---

### 🧩 Agent Capabilities

- General question answering
- Wikipedia-based factual lookup
- Conversational chat
- Joke generation
- Creative writing
- Tool-assisted reasoning

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Get JWT token |
| POST | `/chat` | Chat with the AI agent |
| GET | `/health` | Service health |
| GET | `/test-groq` | Test LLM connection |
| GET | `/test-wikipedia` | Test Wikipedia integration |

---

## ⚙️ Getting Started

### Clone

git clone https://github.com/your-username/your-repo.git

cd your-repo

### Create Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

### Install

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file:

SECRET_KEY=your_secret_key_here

GROQ_API_KEY=your_groq_api_key

FAKE_USERNAME=admin

FAKE_PASSWORD=password

Generate a secret key:

python -c "import secrets; print(secrets.token_hex(32))"

---

## ▶️ Run

uvicorn main:app --reload

API:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Request a JWT token from `/login`
2. Include it in the `Authorization: Bearer <token>` header
3. Access the protected `/chat` endpoint

---

## 🧠 How the Agent Works

User Input

→ ReAct reasoning

→ Tool decision

→ Wikipedia (if required)

→ Final LLM response

For factual questions, the agent retrieves external knowledge before responding. For conversational or creative requests, it answers directly without tool usage.

---

## 🏗️ Architecture

### 🔁 ReAct Workflow

The agent combines reasoning and tool usage within a single ReAct loop.

The LLM is responsible for:

- Understanding user intent
- Deciding whether a tool is needed
- Generating the final response

The system provides:

- Wikipedia integration
- Trace logging
- Controlled tool execution
- Deterministic model settings

This project demonstrates a lightweight ReAct architecture built on FastAPI and LangChain.

---

## 🌐 Wikipedia Retrieval Flow

When factual information is required, the tool follows this process:

1. Attempt direct page lookup
2. Fall back to Wikipedia search
3. Score search candidates
4. Retrieve the best matching summary

---

## 💬 Example Requests

### Direct Response

POST /chat

{ "message": "Tell me a joke" }

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Why don’t scientists trust atoms? Because they make up everything!"
  }
}

---

### Wikipedia Lookup

POST /chat

{ "message": "What is Python?" }

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Wikipedia",
    "action_input": "What is Python?",
    "observation": "...",
    "final_answer": "Python is a high-level, general-purpose programming language..."
  }
}

---

### Creative Request

POST /chat

{ "message": "Write me a short poem" }

Response:

{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Beneath the quiet moon's soft glow..."
  }
}

---

## 🚀 Benefits

- Clean FastAPI architecture
- JWT-secured API
- LangChain ReAct workflow
- Automatic Wikipedia retrieval
- Easy to extend with additional tools
- Useful for learning agent-based systems

---

## 🚧 Current Limitations

- Single external tool (Wikipedia)
- No conversation memory
- Stateless requests
- Demo authentication system

---

## 🚀 Future Improvements

- Conversation memory
- Additional external tools
- Multi-user support
- Token refresh
- Observability and monitoring

---

## 💡 Design Philosophy

> **The agent reasons first, then decides whether external knowledge is needed before responding.**

This project focuses on demonstrating the ReAct pattern, where reasoning and tool usage are combined into a simple decision-making loop. It provides a practical introduction to tool-augmented AI systems while remaining easy to understand and extend.

---

## 🙌 Final Notes

This project demonstrates how FastAPI, JWT authentication, LangChain, Groq LLMs, and Wikipedia can be combined into a lightweight ReAct-style AI agent. While intentionally simpler than a production-grade tool orchestration system, it illustrates the core concepts of reasoning, tool selection, and grounded responses.

---

## 📄 License

MIT License