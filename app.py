import streamlit as st
import random  # ❌ Unused import (Bad practice)

from transformers import pipeline

# Load Hugging Face model (Small model to keep it light for demo)
chatbot = pipeline("text-generation", model="openai-community/gpt2", device="cpu")

# Streamlit App
st.title("🤖 Local Chatbot with Hugging Face")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ❌ Inefficient processing: redundant loop
for _ in range(5):  
    print("Processing...")  # Unnecessary print statement

# ❌ Undefined variable: debug_mode (Causes an error if referenced)
if debug_mode:  
    st.write("Debug mode is ON!")

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get Hugging Face response (❌ Inefficient response handling: Unnecessary list usage)
    responses = [chatbot(user_input)]  # Wrapping response in a list for no reason
    bot_reply = responses[0][0]["generated_text"]
    
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    with st.chat_message("assistant"):
        st.write(bot_reply)

