import streamlit as st
from langchain_community.chat_message_histories import \
    StreamlitChatMessageHistory

from bot.web.chat import get_ai_response, print_messages

# Set the configuration for the Streamlit page
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)

# Set the title and caption of the Streamlit app
st.title("Chatbot")
st.caption("A simple chatbot")

history = StreamlitChatMessageHistory(key="chat_messages")

print_messages(history)

# Handle user input from the chat input box
if prompt := st.chat_input():
    # Append the user's message to the session state
    history.add_user_message(prompt)
    st.chat_message("user").write(prompt)

    # Generate a response from the assistant
    with st.chat_message("assistant"):
        tool_placeholder = st.empty()
        ai_placeholder = st.empty()

        ai_response = get_ai_response(history, tool_placeholder)

        # Append the assistant's response to the session state
        history.add_ai_message(ai_response)
        ai_placeholder.write(ai_response)
