# 📈 AI Chatbot Assistant (InclusionAI Ling 3.0 Flash Fin)

An interactive, full-stack AI Chatbot application built with **Streamlit** and powered by **InclusionAI Ling 3.0 Flash Fin**, an open-source Mixture-of-Experts (MoE) finance-focused AI model.

The application includes a chat interface, multi-turn session history, file text/PDF extraction, and an interactive Jupyter Notebook for step-by-step development.
---

## ✨ Features
- 🤖 **InclusionAI Ling 3.0 Flash Fin Model**: Powered by InclusionAI's finance-focused open-source MoE model via OpenRouter / OpenAI-compatible API.
- 💬 **Interactive Chat Interface**: Clean multi-turn conversation UI built with Streamlit (`st.chat_message`, `st.chat_input`).
- 📄 **Document Analysis**: Upload `.txt` or `.pdf` files in the sidebar and query the AI based on document content.
- 📓 **Jupyter Notebook Tutorial**: Complete step-by-step walkthrough in [`building-chatbot-notebook.ipynb`](./building-chatbot-notebook.ipynb).
- 🛡️ **Environment Config**: Secure API key management via `.env` files.

---

## 📁 Project Structure
```text
agent-with-streamlit-ui/
├── app.py                            # Main Streamlit web application
├── building-chatbot-notebook.ipynb   # Interactive Jupyter Notebook guide
├── requirements.txt                  # Python dependencies
├── .env                              # Template for environment configuration
└── assets/                           # Media & UI screenshots/demo
```

---
## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Engine**: [InclusionAI Ling 3.0 Flash Fin](https://openrouter.ai/)
- **PDF Extraction**: [PyPDF2](https://pypi.org/project/PyPDF2/)
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)
