import logging
from langchain_groq import ChatGroq
from config import GROQ_API_KEY
from tools.wikipedia import wikipedia_tool

logger = logging.getLogger(__name__)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)

# -----------------------------
# ROUTER (safe decision only)
# -----------------------------
def route(query: str) -> str:
    prompt = f"""
Answer only:
wikipedia or none

Question: {query}
"""
    return llm.invoke(prompt).content.strip().lower()


# -----------------------------
# FINAL ANSWER
# -----------------------------
def answer(query: str, context: str = "") -> str:
    prompt = f"""
Answer the question clearly.

Question: {query}

Context:
{context}
"""
    return llm.invoke(prompt).content.strip()


# -----------------------------
# REACT STYLE AGENT
# -----------------------------
def run_agent(query: str):
    try:
        trace = []

        # -------- THOUGHT --------
        thought = "I need to decide if I should use a tool."
        trace.append(f"Thought: {thought}")

        decision = route(query)

        if decision == "wikipedia":
            action = "Wikipedia"
            action_input = query

            trace.append(f"Action: {action}")
            trace.append(f"Action Input: {action_input}")

            observation = wikipedia_tool(query)
            content = observation.get("content", "")

            trace.append(f"Observation: {content}")

            trace.append("Thought: I now have enough information to answer.")
            final = answer(query, content)

        else:
            action = "Direct"
            action_input = ""

            # FIX: ensure variable always exists
            content = "No tool needed"

            trace.append("Action: None")
            trace.append("Observation: No tool needed")

            trace.append("Thought: I will answer directly.")
            final = answer(query)

        trace.append(f"Final Answer: {final}")

        return {
            "response": {
                "thought": thought,
                "action": action,
                "action_input": action_input,
                "observation": content,
                "final_answer": final
            }
        }

    except Exception as e:
        logger.exception("Agent error")
        return {
            "response": {
                "thought": "An error occurred.",
                "action": "Direct",
                "action_input": None,
                "observation": str(e),
                "final_answer": str(e)
            }
        }