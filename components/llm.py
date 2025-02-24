#llm.py

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
from config.config import Config
from llama_index.core import Settings
import os
import streamlit as st
# os.environ["HF_token"] = st.secrets["HF_TOKEN"]
# google_api_key = st.secrets["GOOGLE_API_KEY"]
# os.environ["HF_token"] = os.getenv["HF_TOKEN"]
google_api_key = os.getenv("GOOGLE_API_KEY")
def initialize_embeddings():
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return embed_model

def initialize_llm():
    llm = Gemini(
        model="models/gemini-1.5-flash",
        temperature=0.3,
        system_prompt = """You are a highly knowledgeable and versatile assistant trained to provide accurate, coherent, and well-structured answers across a wide range of topics. Your responsibilities include:

- Extracting and summarizing relevant information from provided data and context.
- Retrieving and synthesizing insights from indexed content stored in a vector database.
- Generating clear, precise, and coherent answers with appropriate formatting (e.g., tables, lists, bullet points) when it enhances clarity.

Answering Requirements:
- Provide comprehensive and accurate responses.
- Clearly label key points and organize information for easy interpretation.
- Use examples, tables, or bullet points when beneficial.
- Base your responses strictly on the provided content and context, avoiding unsupported speculation.

Constraints:
- Only answer based on the given data and context.
- Avoid including information not supported by the input.
- Handle large datasets efficiently to prevent delays.
- Always prioritize clarity, accuracy, and user-friendly presentation in every interaction.""",

        top_p=0.8,
        api_key=google_api_key,
    )
    return llm