# 🚀 FastAPI with JWT Authentication + Groq-Powered Tool-Using LLM

A FastAPI API featuring JWT authentication and a Groq-powered LLM that routes user queries and optionally uses a Wikipedia tool to retrieve factual information.

The system is **ReAct-inspired**, following a structured **Thought → Action → Observation → Final Answer** flow through custom Python logic rather than an agent framework.

The implementation is intentionally lightweight, using only the Groq client interface for LLM calls and custom routing logic.

---

# Version

Local development uses **Python 3.12**.

---

## 📌 Project Info

- Version: 0.0.2
- Python: 3.12
- Framework: FastAPI
- LLM: Groq (`ChatGroq`)
- Architecture: ReAct-inspired router with optional tool execution
- Last Updated: 01-07-2026

---

## 🎯 Use Cases

This project can serve as a foundation for:

- 🤖 AI assistants with tool usage
- ⚡ FastAPI LLM backends
- 🧠 ReAct-inspired reasoning systems
- 🧪 Lightweight AI backend experimentation
- 🎓 Educational agent architecture demos
- 🌐 Knowledge retrieval APIs

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

1. **Thought** – Begin with a reasoning step
2. **Action Decision** – The LLM classifies the request:
   - `wikipedia`
   - `none`
3. **Action Execution** – If required, the Wikipedia tool is called
4. **Observation** – Retrieved information is passed back to the model
5. **Final Answer** – The LLM generates the final response

Key characteristics:

- ReAct-inspired reasoning structure
- Single routing decision per request
- Transparent execution trace
- Deterministic responses (`temperature=0`)
- Lightweight custom implementation

---

### 🧠 LLM Integration

The project uses Groq for inference:

- Client: `ChatGroq`
- Model: `openai/gpt-oss-20b`
- Temperature: `0`
- API key managed through environment variables

The LLM performs two tasks:

- Route whether a tool is needed
- Generate the final response

---

### 🌐 Wikipedia Tool

A lightweight Wikipedia retrieval tool provides factual grounding when required.

Features include:

- Direct page lookup
- Search fallback
- Summary extraction
- Graceful error handling

The tool is only invoked when the router selects it.

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
|---------|----------|-------------|
| POST | `/login` | Get JWT access token |
| POST | `/chat` | Chat with the LLM |
| GET | `/health` | Service health check |
| GET | `/test-groq` | Test Groq connectivity |
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

Generate a secure secret key:

python -c "import secrets; print(secrets.token_hex(32))"

---

## ▶️ Run the Application

uvicorn main:app --reload

API:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Request a JWT token from `/login`
2. Include it in requests:

Authorization: Bearer `<token>`

3. Access the protected `/chat` endpoint

---

## 🧠 System Flow

User Input

↓

LLM Router

↓

Tool Decision

↓

(Optional) Wikipedia Retrieval

↓

Context Injection

↓

Final LLM Response

---

## 🏗️ Architecture

### ReAct-Inspired Design

The system is inspired by the ReAct (Reason + Act) pattern while remaining intentionally simple.

Workflow:

- Generate an initial reasoning step
- Decide whether a tool is required
- Execute the tool if needed
- Feed retrieved information back into the model
- Generate the final response

Unlike full agent frameworks, this implementation:

- Uses no AgentExecutor
- Performs no iterative planning
- Executes at most one tool per request
- Uses straightforward Python functions instead of an orchestration framework

---

## 🌐 Wikipedia Retrieval Flow

When Wikipedia is selected:

1. Attempt direct page lookup
2. Fall back to search
3. Retrieve the best result
4. Extract summary content
5. Use the summary as context for the final answer

---

## 💬 Example Requests

### Direct Response

POST `/chat`

```json
{
  "message": "Tell me a joke"
}
```

Response:

```json
{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Why don't scientists trust atoms? Because they make up everything!"
  }
}
```

---

### Wikipedia Lookup

POST `/chat`

```json
{
  "message": "Who was Ada Lovelace?"
}
```

Response:

```json
{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Wikipedia",
    "action_input": "Who was Ada Lovelace?",
    "observation": "Ada Lovelace was an English mathematician...",
    "final_answer": "Ada Lovelace is widely regarded as one of the first computer programmers..."
  }
}
```

---

### Creative Request

POST `/chat`

```json
{
  "message": "Write me a short poem"
}
```

Response:

```json
{
  "response": {
    "thought": "I need to decide if I should use a tool.",
    "action": "Direct",
    "action_input": "",
    "observation": "No tool needed",
    "final_answer": "Beneath the quiet moon's soft glow..."
  }
}
```

---

## 🚀 Benefits

- Clean FastAPI architecture
- JWT-secured API
- Lightweight LLM integration
- Transparent reasoning trace
- Optional factual grounding with Wikipedia
- Easy to extend with additional tools
- Minimal dependencies

---

## 🚧 Current Limitations

- Single external tool (Wikipedia)
- No conversation memory
- Stateless requests
- One routing decision per request
- Single-step execution
- Demo authentication system

---

## 🚀 Future Improvements

- Conversation memory
- Additional tools
- Multi-step planning
- Streaming responses
- Logging and observability
- Production-ready authentication
- Configurable routing policies

---

## 💡 Design Philosophy

> This project demonstrates a lightweight approach to tool-using LLMs using straightforward Python functions instead of a full agent framework.

The design prioritizes:

- Simplicity
- Readability
- Transparency
- Deterministic behavior
- Easy extensibility

---

## 🙌 Final Notes

This project demonstrates how FastAPI, JWT authentication, Groq-powered language models, and a Wikipedia retrieval tool can be combined into a lightweight ReAct-inspired AI backend.

Rather than relying on a complex orchestration framework, the routing, tool execution, and response generation are implemented with simple Python functions, making the project easy to understand, debug, and extend.

---

## 📄 License

MIT License.