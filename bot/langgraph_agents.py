from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langgraph.prebuilt import create_react_agent

from bot.models import ChatModelFactory
from bot.tools import today


def init_langgraph_agent(
    provider: str,
    model_name: str,
):

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

    tools = load_tools(["ddg-search", "read_file"])
    tools.append(today)

    model = ChatModelFactory.get_llm(provider, model_name)

    langgraph_agent_executor = create_react_agent(
        model=model,
        tools=tools,
        state_modifier=prompt,
    )

    return langgraph_agent_executor


def stream_langgraph_agent(
    agent_executor: Runnable,
    question: str,
):
    for s in agent_executor.stream(
        {
            "messages": [("human", question)],
        },
        stream_mode="values",
    ):
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

    return "Done"
