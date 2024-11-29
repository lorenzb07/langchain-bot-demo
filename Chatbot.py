import os
from datetime import datetime

import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

from bot.agents import init_agent

# Set the configuration for the Streamlit page
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)

# Set the title and caption of the Streamlit app
st.title("Chatbot")
st.caption("A simple chatbot")

# Initialize the session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        # {"role": "assistant", "content": "Hello! How can I help you?"}
    ]

# Display all messages in the session state
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input from the chat input box
if prompt := st.chat_input():
    # Append the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate a response from the assistant
    with st.chat_message("assistant"):

        # Initialize the Streamlit callback handler
        st_callback = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=True,
        )

        # Get the agent executor for the Azure OpenAI service
        agent_executor = init_agent(
            provider=os.getenv("STREAMLIT_LLM_PROVIDER"),
            model_name=os.getenv("STREAMLIT_LLM_MODEL"),
            with_history=True,
        )
        response = agent_executor.invoke(
            {
                "input": prompt,
                "today": datetime.now().strftime("%Y-%m-%d"),
                "chat_history": st.session_state.messages,
            },
            {
                "callbacks": [st_callback],
            },
        )

        # Extract the output from the response
        out = response["output"]
        st.write(out)

        # Append the assistant's response to the session state
        st.session_state.messages.append({"role": "assistant", "content": out})
