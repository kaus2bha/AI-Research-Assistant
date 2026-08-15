import os
import certifi

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from tools import tools


# -----------------------------
# Environment
# -----------------------------

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)


# -----------------------------
# Prompt
# -----------------------------

prompt = hub.pull("hwchase17/react")


# -----------------------------
# Create Agent
# -----------------------------

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


# -----------------------------
# Agent Executor
# -----------------------------

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


# -----------------------------
# Run Agent
# -----------------------------

def run_agent(
    user_input: str,
    chat_history: list
) -> str:

    history_text = ""

    for message in chat_history:
        role = message["role"].upper()
        content = message["content"]

        history_text += f"{role}: {content}\n"

    contextual_input = (
        "Conversation history:\n"
        f"{history_text}\n"
        "Current user request:\n"
        f"{user_input}"
    )

    response = agent_executor.invoke({
        "input": contextual_input
    })

    return response["output"]