# components/ui.py
import os
import tempfile
import logging
import streamlit as st
import nest_asyncio
from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from components.data_loader import load_and_enhance_documents, load_documents_from_urls
from components.llm import initialize_embeddings, initialize_llm

import tempfile

nest_asyncio.apply()
logger = logging.getLogger(__name__)

def display_content_ingestion():
    st.header("Content Ingestion")
    st.write("Upload PDF files **or** input URLs to ingest text content. New content will be added to your existing index.")

    input_type = st.radio("Choose Input Type", ["PDF Upload", "URL Input"], key="input_type")
    new_nodes = []
    
    if input_type == "PDF Upload":
        uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type=["pdf"])
        if uploaded_files:
            with st.spinner("Processing PDF files..."):
                temp_files = []
                for uploaded_file in uploaded_files:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                        temp_file.write(uploaded_file.read())
                        temp_files.append(temp_file.name)
                        logger.info(f"Temporary file created: {temp_file.name}")
                enhanced_documents = load_and_enhance_documents(temp_files)
                documents = [Document(text=doc.text, metadata=doc.metadata) for doc in enhanced_documents]
                node_parser = SentenceWindowNodeParser.from_defaults(
                    window_size=40,
                    window_metadata_key="window",
                    original_text_metadata_key="original_sentence",
                )
                new_nodes = node_parser.get_nodes_from_documents(documents)
                
    else:  # URL Input
        urls = st.text_area("Enter one URL per line", height=150)
        if st.button("Process URLs"):
            if urls.strip():
                url_list = [url.strip() for url in urls.splitlines() if url.strip()]
                with st.spinner("Fetching and processing URLs..."):
                    documents = load_documents_from_urls(url_list)
                    if documents:
                        node_parser = SentenceWindowNodeParser.from_defaults(
                            window_size=40,
                            window_metadata_key="window",
                            original_text_metadata_key="original_sentence",
                        )
                        new_nodes = node_parser.get_nodes_from_documents(documents)
                    else:
                        st.error("No valid content was fetched from the URLs.")
            else:
                st.warning("Please enter at least one URL.")
    
    if new_nodes:
        # Merge new nodes with previously ingested nodes
        if "all_nodes" in st.session_state:
            st.session_state["all_nodes"].extend(new_nodes)
        else:
            st.session_state["all_nodes"] = new_nodes
        # Rebuild the index with the cumulative nodes
        st.session_state["index"] = VectorStoreIndex(st.session_state["all_nodes"], use_async=True)
        st.success("Content ingested successfully! You can now ask questions.")

def display_query_interface(index):
    st.header("Ask a Question")
    if not index:
        st.info("Please ingest some content first in the 'Content Ingestion' mode.")
        return

    query_engine = index.as_chat_engine(
        similarity_k=3,
        chat_mode="context",
        node_postprocessors=[MetadataReplacementPostProcessor(target_metadata_key="window")]
    )
    user_query = st.text_input("Enter your query:")
    if st.button("Submit Query") and user_query:
        with st.spinner("Processing query..."):
            response = query_engine.chat(user_query)
            if response:
                st.markdown("### Response")
                # Extract only the final answer text
                final_answer = response.response if hasattr(response, "response") else str(response)
                st.write(final_answer)
                st.markdown("### Retrieved Context")
                for node in response.source_nodes:
                    with st.expander(f"Source: {node.metadata.get('source', 'Document')}"):
                        st.write(node.text)
            else:
                st.error("No response returned for the query.")


def initialize_models():
    # Initialize LLM and embeddings and update global Settings
    llm = initialize_llm()
    embed_model = initialize_embeddings()
    Settings.llm = llm
    Settings.embed_model = embed_model
