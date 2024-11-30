import os

import streamlit as st

from bot.langgraph_agents import init_langgraph_agent
from bot.web.callback import get_streamlit_cb


def print_messages(history):
    for msg in history.messages:
        st.chat_message(msg.type).write(msg.content)


def get_ai_response(history, tool_placeholder):
    # Initialize the Streamlit callback handler
    st_callback = get_streamlit_cb(
        tool_placeholder,
    )

    # Get the agent executor for the Azure OpenAI service
    agent_executor = init_langgraph_agent(
        provider=os.getenv("STREAMLIT_LLM_PROVIDER"),
        model_name=os.getenv("STREAMLIT_LLM_MODEL"),
    )

    # Invoke the agent executor with the user's input
    response = agent_executor.invoke(
        input={
            "messages": history.messages,
        },
        config={
            "callbacks": [st_callback],
        },
    )

    # Extract the output from the response
    return response["messages"][-1].content
