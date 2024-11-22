from bot.models import ChatModelFactory
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentExecutor, create_react_agent

from langchain_core.prompts import PromptTemplate
from datetime import datetime

from bot.prompts import PROMPT_TEMPLATE

def run_agent(
        model_name: str,
        question: str,
):
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)

    tools = load_tools(["ddg-search"])

    model = ChatModelFactory.get_model(model_name)

    agent = create_react_agent(model, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,
    )

    for chunk in agent_executor.stream(
            {
                "input": question,
                "today": datetime.now().strftime("%Y-%m-%d"),
            }
    ):
        print(chunk)
        print("----")
        if chunk.get("output"):
            return chunk["output"]




# TODO: add streamlit: https://python.langchain.com/docs/integrations/callbacks/streamlit/