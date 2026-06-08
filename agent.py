import logging
from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor, Tool
from langchain_core.prompts import PromptTemplate

from config import GROQ_API_KEY
from tools.wikipedia import wikipedia_tool as wiki_func

logger = logging.getLogger(__name__)

# ------------------------------
# LLM
# ------------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)

# ------------------------------
# Tools
# ------------------------------
tools = [
    Tool(
        name="Wikipedia",
        func=wiki_func,
        description="Use ONLY for factual questions that require encyclopedic knowledge."
    )
]

# ------------------------------
# Improved Prompt (FIXED ReAct behavior)
# ------------------------------
prompt = PromptTemplate.from_template("""
You are a helpful assistant.

You have access to tools, but you must use them carefully.

AVAILABLE TOOLS:
{tools}

TOOL NAMES:
{tool_names}

CRITICAL RULES:
- Use the Wikipedia tool ONLY for factual questions (definitions, history, explanations).
- If the user asks for jokes, greetings, opinions, or creative writing:
  → DO NOT use any tool
  → Respond directly with Final Answer
- NEVER output "Action: None"
- NEVER attempt to call a tool if it is not needed

DECISION RULE:
- If tool is needed → follow tool format
- If tool is NOT needed → go directly to Final Answer

---

FORMAT (ONLY when using a tool):

Question: {input}
Thought: I need to use a tool
Action: Wikipedia
Action Input: the user question
Observation: result
Final Answer: response

---

FORMAT (when NOT using a tool):

Question: {input}
Thought: no tool is needed
Final Answer: direct response

---

Question: {input}

{agent_scratchpad}
""")

# ------------------------------
# Agent
# ------------------------------
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=2,
    early_stopping_method="force",
    handle_parsing_errors=True
)

# ------------------------------
# Wrapper
# ------------------------------
def run_agent(query: str):
    try:
        result = agent_executor.invoke({"input": query})

        output = result.get("output") if isinstance(result, dict) else str(result)

        return {"response": output}

    except Exception as e:
        logger.error(f"Agent error: {e}")
        return {"response": f"Agent error: {str(e)}"}