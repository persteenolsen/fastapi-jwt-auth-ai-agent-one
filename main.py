import os
import time
import uuid
import logging
import traceback

from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv
import jwt

from langchain_groq import ChatGroq

# Note: The below import path does not work !
# from langchain_classic.agents import create_react_agent, AgentExecutor

# Note: This below import works !
from langchain.agents import create_react_agent, AgentExecutor

from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper

# --------------------------------------------------
# ENV + LOGGING
# --------------------------------------------------
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
FAKE_USERNAME = os.getenv("FAKE_USERNAME")
FAKE_PASSWORD = os.getenv("FAKE_PASSWORD")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

required_env_vars = ["SECRET_KEY", "FAKE_USERNAME", "FAKE_PASSWORD", "GROQ_API_KEY"]
for var in required_env_vars:
    if not os.getenv(var):
        raise RuntimeError(f"Missing environment variable: {var}")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------
app = FastAPI(
    title="AI Agent API (Groq + JWT + Safe Wikipedia + ReAct)",
    description="07-06-2026 - Secure AI agent API using FastAPI, JWT auth, Groq LLM, and a safe Wikipedia tool. Designed to prevent infinite loops and ensure reliability on Vercel.",
    version="0.0.3", 
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

security = HTTPBearer()

# --------------------------------------------------
# MODELS
# --------------------------------------------------
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# --------------------------------------------------
# JWT
# --------------------------------------------------
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username != FAKE_USERNAME:
            raise HTTPException(status_code=401, detail="Invalid user")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --------------------------------------------------
# LOGIN
# --------------------------------------------------
@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    if request.username != FAKE_USERNAME or request.password != FAKE_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    token = create_access_token(
        {"sub": request.username},
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return TokenResponse(access_token=token)

# --------------------------------------------------
# GROQ LLM
# --------------------------------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)

# --------------------------------------------------
# SAFE WIKIPEDIA (FIXED)
# --------------------------------------------------

# WikipediaAPIWrapper is a LangChain utility that performs
# searches against Wikipedia and returns summarized content.
#
# top_k_results=2:
# Limits the number of articles returned. This helps
# reduce unnecessary context and keeps responses concise.
#
# timeout=8:
# Prevents requests from hanging too long, which is important
# in serverless environments such as Vercel.
#
# Custom User-Agent:
# Some external services reject requests that do not provide
# a user-agent header.
wiki_api = WikipediaAPIWrapper(
    top_k_results=2,
    requests_kwargs={
        "headers": {"User-Agent": "Mozilla/5.0 (AI-Agent)"},
        "timeout": 8
    }
)

def safe_wikipedia(query: str) -> str:
    """
    Safe wrapper around Wikipedia.

    The ReAct agent may call this function whenever it decides
    additional factual information is required.

    Responsibilities:
    - Execute Wikipedia lookup
    - Log requests
    - Handle failures gracefully
    - Prevent tool retry loops

    Returning a string instead of raising an exception is
    important because many agent frameworks interpret tool
    failures as a signal to retry the same tool repeatedly.
    """

    try:
        logger.info(f"Wikipedia query: {query}")

        # Execute Wikipedia search
        result = wiki_api.run(query)

        # Handle empty results gracefully
        if not result or len(result.strip()) == 0:
            return "Wikipedia returned no results."

        return result

    except Exception as e:
        logger.error("Wikipedia failed")
        logger.error(traceback.format_exc())

        # IMPORTANT:
        #
        # Do not raise the exception back to the agent.
        # Instead return a normal observation string.
        #
        # This allows the agent to continue reasoning
        # and avoids endless retry loops.
        return (
            "Wikipedia temporarily unavailable. "
            "Please answer from general knowledge instead."
        )

# Tool exposed to the ReAct agent.
#
# The LLM never directly calls Python functions.
# LangChain exposes functions as tools containing:
#
# - Name
# - Description
# - Callable function
#
# Example:
#
# Action: wikipedia
# Action Input: Capital of France
#
# becomes:
#
# safe_wikipedia("Capital of France")
#
wiki_tool = Tool(
    name="wikipedia",
    func=safe_wikipedia,
    description="Use ONLY for factual lookup of real-world information."
)

# List of tools available to the agent.
# Additional tools could be added later:
# - Calculator
# - Weather API
# - Company database
# - Vector search
tools = [wiki_tool]


# --------------------------------------------------
# PROMPT (STABLE REACT FORMAT)
# --------------------------------------------------

# ReAct = Reason + Act
#
# Instead of immediately generating an answer,
# the model follows a structured workflow:
#
# Thought:
#     Decide what to do.
#
# Action:
#     Select a tool.
#
# Observation:
#     Receive tool output.
#
# Thought:
#     Continue reasoning.
#
# Final Answer:
#     Return response to the user.
#
# LangChain automatically injects:
#
# {tools}
#     Human-readable descriptions of available tools.
#
# {tool_names}
#     Valid tool names available for Action steps.
#
# {agent_scratchpad}
#     Previous Thought/Action/Observation history.
#
# This scratchpad is what allows the model to continue
# reasoning after a tool call.
#


template = """
You are a helpful assistant with access to tools.

You must follow the ReAct format strictly.

TOOLS:
{tools}

TOOL NAMES:
{tool_names}

RULES:
- Use tools ONLY if necessary for factual lookup.
- Do NOT use tools for jokes, greetings, or creative answers.
- If you already know the answer, respond immediately.
- NEVER loop more than once.

FORMAT:

Question: {input}
Thought: decide if tool is needed

If using tool:
Action: one of [{tool_names}]
Action Input: input for tool
Observation: result

Then:
Thought: final reasoning
Final Answer: final answer

If NOT using tool:
Final Answer: answer directly

Begin!

Question: {input}
{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# --------------------------------------------------
# AGENT (FIXED SAFE SETTINGS)
# --------------------------------------------------

# create_react_agent() builds a ReAct agent.
#
# Components:
#
# llm
#     The language model responsible for reasoning.
#
# tools
#     External capabilities available to the model.
#
# prompt
#     Instructions defining how reasoning occurs.
#
# The agent itself does not execute tool calls.
# It only decides what should happen next.
#
# Example:
#
# User:
#     "Who invented Python?"
#
# Agent:
#     Thought: I need factual information.
#
#     Action: wikipedia
#
#     Action Input: Who invented Python
#
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# AgentExecutor is responsible for running the full
# Thought -> Action -> Observation loop.
#
# Execution flow:
#
# User
#   |
#   v
# AgentExecutor
#   |
#   +--> LLM Thought
#   |
#   +--> Tool Call
#   |
#   +--> Observation
#   |
#   +--> More Reasoning
#   |
#   +--> Final Answer
#   |
#   v
# Response
#
# The executor keeps running until:
#
# - Final Answer is produced
# - Iteration limit is reached
# - An unrecoverable error occurs
#
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,

    # Prevents infinite loops where the model
    # repeatedly calls tools without producing
    # a final answer.
    max_iterations=3,

    # If the iteration limit is reached,
    # force the best possible answer instead
    # of raising an exception.
    early_stopping_method="force",

    # If the model generates malformed ReAct syntax,
    # LangChain attempts recovery rather than failing.
    handle_parsing_errors=True
)
# --------------------------------------------------
# CHAT ENDPOINT (SAFE)
# --------------------------------------------------
# Main protected endpoint.
#
# Complete request flow:
#
# 1. Client sends JWT token.
# 2. verify_token() validates authentication.
# 3. User message is received.
# 4. AgentExecutor starts the ReAct cycle.
# 5. Agent decides whether tools are needed.
# 6. Tool results are returned as observations.
# 7. Agent generates Final Answer.
# 8. API returns response.
#
# Example:
#
#     User:
#         "Who invented Python?"
#
#     Agent:
#         Thought -> Need factual lookup
#
#         Action -> wikipedia
#
#         Observation -> Wikipedia result
#
#         Thought -> I now know the answer
#
#         Final Answer -> Returned to client
@app.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    user: str = Depends(verify_token)
):

    start = time.time()

    try:
        logger.info(f"User: {user}, Message: {request.message}")

        # Start the full ReAct execution cycle.
        #
        # The agent may:
        # - answer immediately
        # - call Wikipedia
        # - reason over tool output
        #
        result = agent_executor.invoke({
            "input": request.message
        })

        logger.info(
            f"Completed in {time.time() - start:.2f}s"
        )

        # LangChain returns a dictionary.
        #
        # For ReAct agents the final response is
        # available under the "output" key.
        return ChatResponse(
            response=result["output"]
        )

    except Exception as e:
        error_id = str(uuid.uuid4())

        logger.error(f"Error ID: {error_id}")
        logger.error(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail={
                "error_id": error_id,
                "type": type(e).__name__,
                "message": str(e)
            }
        )

# --------------------------------------------------
# HEALTH CHECKS
# --------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "groq": bool(GROQ_API_KEY),
        "secret": bool(SECRET_KEY)
    }

@app.get("/test-groq")
def test_groq():
    try:
        res = llm.invoke("Tell me a joke")
        return {"status": "ok", "response": res.content}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/test-wikipedia")
def test_wikipedia():
    try:
        return {"status": "ok", "result": safe_wikipedia("Capital of France")}
    except Exception as e:
        return {"status": "failed", "error": str(e)}