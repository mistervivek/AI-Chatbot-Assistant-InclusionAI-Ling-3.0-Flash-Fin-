# app.py (full code combining all steps)

import os
import openai
import streamlit as st
import PyPDF2
from dotenv import load_dotenv

load_dotenv(override=True)  # Load and override environment variables from .env

# Configure LLM credentials for InclusionAI Ling 3.0 Flash Fin (via OpenRouter)
api_key = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or "dummy-key"
base_url = os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("LLM_MODEL", "inclusionai/ling-3.0-flash-fin")

client_args = {"api_key": api_key}
if base_url:
    client_args["base_url"] = base_url

client = openai.OpenAI(**client_args)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

# Function to process the uploaded file
def process_uploaded_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        return uploaded_file.getvalue().decode("utf-8")
    else:
        return "Unsupported file type. Please upload a TXT or PDF file."

# Define a function to generate a response from the AI given a user message
def generate_response(user_prompt, file_content=None):
    """
    Sends the user prompt to the InclusionAI Ling 3.0 Flash Fin model and returns the response.

    Parameters:
    -----------
    user_prompt : str
        The input message from the user.
    file_content : str, optional
        Content extracted from an uploaded file.

    Returns:
    --------
    str
        The AI-generated response as plain text.
    """
    messages = []
    
    # If file content is provided, add it as context
    if file_content:
        messages.append({
            "role": "system", 
            "content": f"The user has uploaded a file with the following content:\n\n{file_content}\n\nPlease consider this information when responding to their financial/analytical query."
        })
    
    # Add the user's prompt
    messages.append({"role": "user", "content": user_prompt})
    
    # Use OpenAI-compatible chat completion endpoint
    response = client.chat.completions.create(
        model=model_name,  # InclusionAI Ling 3.0 Flash Fin model
        messages=messages
    )
    # Extract the assistant's message from the response
    message_text = response.choices[0].message.content
    return message_text  # Return the assistant's reply


st.set_page_config(page_title="Ling 3.0 Flash Fin Assistant", page_icon="📈", layout="wide")
st.title("📈 Ling 3.0 Flash Fin AI Assistant")
st.markdown("**Welcome!** Powered by InclusionAI's **Ling 3.0 Flash Fin** open-source MoE finance model. Ask questions or upload financial/text documents for analysis.")

# File upload section in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload a file (optional):", type=["txt", "pdf"])
file_content = None

if uploaded_file is not None:
    st.sidebar.write("Uploaded file:", f"**{uploaded_file.name}** ({uploaded_file.size} bytes)")
    
    # Process the file and store its content
    with st.sidebar.spinner("Processing file..."):
        file_content = process_uploaded_file(uploaded_file)
    
    # Show a preview of the file content
    with st.sidebar.expander("File Content Preview"):
        st.write(file_content[:500] + "..." if len(file_content) > 500 else file_content)

if "messages" not in st.session_state:
    st.session_state.messages = []
if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I am Ling 3.0 Flash Fin, a finance-focused AI agent. How can I assist you today?"})

# Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input widget for new messages
if user_msg := st.chat_input("Type your financial or general message here..."):
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.markdown(user_msg)
    # Generate assistant response with spinner
    with st.chat_message("assistant"):
        with st.spinner("Analyzing with Ling 3.0 Flash Fin..."):
            assistant_msg = generate_response(user_msg, file_content)
            st.markdown(assistant_msg)
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})