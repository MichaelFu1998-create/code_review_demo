import streamlit as st
from transformers import pipeline
import os 

# Load Hugging Face model (Small model to keep it light for demo)
chatbot = pipeline("text-generation", model="openai-community/gpt2", device="cpu")

# Streamlit App
st.title("🤖 Local Chatbot with Hugging Face")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "":
        if message["role"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    if len(user_input) > 0:
        if user_input != "":
            # Append user message
            st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    bot_reply = chatbot("Hello")[0]["generated_text"]  # always responds "Hello"
    
    # Append bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    # Display bot reply
    with st.chat_message("assistant"):
        st.write(bot_reply)

_var = 123  # Not used anywhere