# components/data_loader.py
import os
import json
import logging
import pdfplumber
import requests
from bs4 import BeautifulSoup
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import SimpleDirectoryReader, Document

logger = logging.getLogger(__name__)

def parse_pdf_tables(file_path):
    tables = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                for table in page_tables:
                    tables.append(table)
    except Exception as e:
        logger.error(f"Error parsing PDF tables from {file_path}: {e}")
    return tables

def extract_tables(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    tables = []
    if file_ext == ".pdf":
        tables = parse_pdf_tables(file_path)
    return tables

def load_and_enhance_documents(file_list):
    loader = SimpleDirectoryReader(input_files=file_list)
    documents = loader.load_data()
    for document, file_path in zip(documents, file_list):
        tables = extract_tables(file_path)
        if tables:
            document.metadata["tables"] = json.dumps(tables)
    return documents

# def load_documents_from_urls(url_list):
#     """Fetch and extract text content from URLs."""
#     documents = []
#     for url in url_list:
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.text, 'html.parser')
#                 text = soup.get_text(separator="\n", strip=True)
#                 doc = Document(text=text, metadata={"source": url})
#                 documents.append(doc)
#             else:
#                 logger.error(f"Failed to fetch {url}: {response.status_code}")
#         except Exception as e:
#             logger.error(f"Error processing URL {url}: {e}")
#     return documents

def load_documents_from_urls(url_list):
    """Fetch and extract text content from URLs using llama_index's built-in loader."""
    reader = SimpleWebPageReader()
    # Depending on your llama_index version, the loader expects either a list of URLs or a keyword argument.
    # Here, we assume it accepts a list.
    documents = reader.load_data(urls=url_list)
    return documents