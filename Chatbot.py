# Streamlit + langchain + Ollama (LLLM : gemma2:2b)

import os
import streamlit as st

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --------- Gradient Background Styling ---------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        background-size: 200% 200%;
        animation: gradientMove 10s ease infinite;
        color: white;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    h1, h2, h3, h4, p, label {
        color: white !important;
        text-align: center;
    }

    .stTextInput>div>div>input {
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
    }

    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #ff1e1e;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------- Step 1 : Create Prompt Template ---------

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant who answers questions about the world."),
        ("human", "Question: {question}")
    ]
)

# --------- Step 2 : Streamlit UI ---------

st.title("🤖 Chatbot with Streamlit + LangChain + Ollama")

input_text = st.text_input("Ask a question about the world :")

# --------- Load the Ollama model ---------

ollama = Ollama(model="gemma2:2b", temperature=0.7)

# Convert output model to string
output_parser = StrOutputParser()

# --------- Step 3 : Create LangChain pipeline ---------

chain = prompt | ollama | output_parser

# --------- Step 4 : Run the model ---------

if input_text:
    response = chain.invoke({"question": input_text})
    st.write("💬 Response:")
    st.write(response)
