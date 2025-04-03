import streamlit as st
from transformers import pipeline

# Load Hugging Face model (Small model to keep it light for demo)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-small")

# Streamlit App
st.title("🤖 Local Chatbot with Hugging Face")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get Hugging Face response
    bot_reply = chatbot(user_input)["generated_text"]
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    with st.chat_message("assistant"):
        st.write(bot_reply)
