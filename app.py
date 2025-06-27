import streamlit as st
from ollama_client import OllamaClient

st.set_page_config(page_title="Ollama Chat Playground", layout="wide")

st.title("Ollama Chat Playground")

# Select Model
model = st.selectbox("Select Ollama Model", options=[
    "llama3", 
    "deepseek-r1:latest", 
    "mistral", 
    "codellama:instruct", 
    "gemma:instruct"
], index=1)

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
user_input = st.chat_input("Ask your question...")
if user_input:
    client = OllamaClient(model=model)
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        response = client.send_prompt(user_input)
    st.session_state.chat_history.append(("assistant", response))

# Render chat
for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("assistant"):
            st.markdown(message)
