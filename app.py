# app.py
import streamlit as st
import logging
from components.ui import display_content_ingestion, display_query_interface, initialize_models

# Ensure set_page_config is the very first Streamlit command
st.set_page_config(page_title="Web Content Q&A Tool", page_icon="💡")

# Add a creative logo in the sidebar (ensure logo.png exists in your project or replace with a URL)
st.sidebar.image("logo.png", width=150)
st.sidebar.title("Navigation")

# Sidebar navigation and controls
mode = st.sidebar.radio("Select Mode", ["Content Ingestion", "Ask Questions"])
if st.sidebar.button("Clear All Content"):
    st.session_state.pop("index", None)
    st.session_state.pop("all_nodes", None)
    st.success("Content cleared! Please ingest content again.")

if "index" not in st.session_state:
    st.session_state["index"] = None

# Load LLM and embedding models (ensure your initialize_models() sets them in Settings)
initialize_models()

# Main content display based on mode
if mode == "Content Ingestion":
    display_content_ingestion()
elif mode == "Ask Questions":
    display_query_interface(st.session_state.get("index"))

# Optionally, add a footer for extra creativity
st.markdown("<hr><p style='text-align: center;'>© 2025 Your Company Name. All rights reserved.</p>", unsafe_allow_html=True)
