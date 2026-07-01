# 🚀 FastAPI with JWT Authentication + ReAct-Inspired LangChain Tool-Using LLM

A FastAPI API featuring JWT authentication and a Groq-powered **LangChain-based LLM system** that routes user queries and optionally uses a Wikipedia tool to retrieve factual information.

The system is **ReAct-inspired**, meaning it follows a structured *Thought → Action → Observation → Answer* style trace, but implemented in a lightweight way rather than a full multi-step agent loop.

It uses LangChain’s `ChatGroq` interface for model interaction and a custom routing + tool execution flow.

---

# Version

Local development uses **Python 3.12**.

---

## 📌 Project Info

- Version: 0.0.2
- Python: 3.12
- Framework: FastAPI
- LLM Interface: LangChain (`ChatGroq`)
- Architecture: ReAct-inspired LLM router with tool execution
- Last Updated: 01-07-2026

---

## 🎯 Use Cases

This project can serve as a foundation for:

- 🤖 AI assistants with tool usage
- ⚡ FastAPI LLM backends
- 🧠 ReAct-inspired reasoning systems
- 🧪 LangChain experimentation projects
- 🎓 Educational agent architecture demos
- 🌐 Lightweight knowledge retrieval APIs

---

## ✨ Key Features

### 🔐 Authentication

- JWT authentication (HS256)
- Protected `/chat` endpoint
- Token-based access control
- Environment-based configuration

---

### 🤖 ReAct-Inspired LLM System

The system follows a simplified ReAct-style flow:

1. **Thought** – The system assumes a reasoning step before acting
2. **Action Decision** – The LLM classifies the request:
   - `wikipedia`
   - `none`
3. **Action Execution** – If needed, Wikipedia tool is called
4. **Observation** – Retrieved context is passed back to the model
5. **Final Answer** – LLM generates response using available information

Key properties:

- ReAct-inspired reasoning structure (not full iterative agent loop)
- Single-step tool decision routing
- Transparent execution trace
- Deterministic behavior via temperature=0
- LangChain-powered LLM interface

---

### 🧠 LangChain Integration (Groq)

This project uses LangChain as the LLM abstraction layer:

- `ChatGroq` from `langchain_groq`
- Model: `openai/gpt-oss-20b`
- Temperature: 0 (deterministic output)
- API key managed via environment variables

Used for:

- Tool routing decision
- Final answer generation

---

### 🌐 Wikipedia Tool (Tool-Augmented LLM)

A lightweight Wikipedia retrieval tool provides factual grounding:

- Direct page lookup attempt
- Search fallback mechanism
- Basic result selection
- Error-safe response handling

The tool is invoked only when the LLM route decides it is needed.

---

## 🧩 System Capabilities

- General question answering
- Wikipedia-based factual retrieval
- Conversational chat
- Joke generation
- Creative writing
- Lightweight tool-assisted reasoning

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Get JWT access token |
| POST | `/chat` | Chat with the ReAct-inspired LLM system |
| GET | `/health` | Service health check |
| GET | `/test-groq` | Test LLM connectivity |
| GET | `/test-wikipedia` | Test Wikipedia tool |

---

## ⚙️ Getting Started

### Clone Repository

git clone https://github.com/your-username/your-repo.git

cd your-repo

---

### Create Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

---

### Install Dependencies

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

## ▶️ Run Application

uvicorn main:app --reload

API base URL:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Obtain JWT token from `/login`
2. Include token in requests:

Authorization: Bearer <token>

3. Access `/chat` endpoint

---

## 🧠 System Flow

User Input  
→ LangChain LLM (routing decision)  
→ Optional Wikipedia tool execution  
→ Context injection  
→ Final LangChain LLM response  

---

## 🏗️ Architecture

### 🔁 ReAct-Inspired Design (Simplified)

This system is inspired by the ReAct (Reason + Act) paradigm:

- The model performs an internal “thought” step
- It decides whether a tool is needed
- A single tool (Wikipedia) may be executed
- The result is fed back into the LLM
- A final response is generated

Unlike full ReAct agent frameworks, this implementation:
- Does NOT use iterative tool loops
- Does NOT use AgentExecutor or multi-step planning
- Uses a single routing decision per request

---

## 🌐 Wikipedia Retrieval Flow

When Wikipedia is selected:

1. Attempt direct page lookup
2. Fall back to search query
3. Rank/select best result
4. Extract summary content
5. Pass context to LLM for final answer

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
    "observation": "Python is a high-level programming language...",
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
- LangChain LLM integration
- ReAct-inspired structured reasoning trace
- Wikipedia tool for factual grounding
- Easy to extend with additional tools

---

## 🚧 Current Limitations

- Single external tool (Wikipedia)
- No memory or conversation state
- Stateless request handling
- Single-step routing (not iterative agent loop)
- Demo-level authentication system

---

## 🚀 Future Improvements

- Add conversation memory
- Expand tool ecosystem
- Multi-step ReAct agent loop (true agent upgrade)
- Streaming responses
- Observability + tracing tools
- Multi-user authentication system

---

## 💡 Design Philosophy

> This system is a lightweight, ReAct-inspired LLM router built using LangChain abstractions and a simple tool execution layer.

It prioritizes:
- clarity over complexity
- debuggability over autonomy
- structured control over full agent freedom

---

## 🙌 Final Notes

This project demonstrates how FastAPI, JWT authentication, LangChain (`ChatGroq`), and a Wikipedia tool can be combined into a **ReAct-inspired tool-using LLM system**.

It is intentionally simplified to make the core ideas of routing, tool usage, and structured reasoning easy to understand and extend.

---

## 📄 License

MIT License