######################################################
# define prompt
######################################################
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the following questions as best you can. Answer in the user's language.",
        ),
        (
            "placeholder",
            "{messages}",
        ),
    ]
)

######################################################
# define model
######################################################
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_retries=2,
    # eventuali altri parametri...
)

######################################################
# define model (example 2)
######################################################
from langchain_groq import ChatGroq

model_2 = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_retries=2,
    # altri parametri...
)

######################################################
# define a simple tool
######################################################
from datetime import datetime

from langchain_core.tools import tool


@tool
def today():
    """
    Get the current date in the format YYYY-MM-DD.

    Returns:
        str: The current date in the format YYYY-MM-DD.
    """
    return datetime.now().strftime("%Y-%m-%d")


######################################################
# load tools
######################################################
from langchain_community.agent_toolkits.load_tools import load_tools

tools = load_tools(["ddg-search", "read_file"])
tools.append(today)

######################################################
# create agent
######################################################
from langgraph.prebuilt import create_react_agent

agent_executor = create_react_agent(
    llm=model,
    tools=tools,
    state_modifier=prompt,
)

######################################################
# run agent
######################################################
user_question = "Che giorno è oggi?"

for s in agent_executor.stream(
    {
        "messages": [("human", user_question)],
    },
    stream_mode="values",
):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()
