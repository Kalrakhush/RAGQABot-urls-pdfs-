# README

## Financial QA Bot on Profit & Loss (P&L) Data

### Overview
This repository contains the source code for a QA bot designed to analyze Profit & Loss (P&L) data from uploaded PDF documents. The bot provides an interactive interface for users to query financial data in real time, leveraging advanced NLP models and indexing techniques.

---

## Features

- **Upload Multiple PDFs:** Users can upload multiple PDF files containing financial data.
- **Query Financial Information:** Enter queries to extract specific financial insights.
- **Display Relevant Results:** Responses are displayed with relevant excerpts from the uploaded documents.
- **State-of-the-Art Models:** Utilizes the Gemini-1.5-flash LLM and BAAI/bge-small-en-v1.5 embedding model.
- **Asynchronous Processing:** Handles large datasets and multiple queries efficiently.

---

## System Requirements

- **Python Version:** Python 3.8 or later
- **Libraries:**
  - Streamlit
  - pdfplumber
  - llama_index
  - HuggingFace Transformers
  - Nest Asyncio

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd financial-qa-bot
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Initialize Models:**
   - Modify the `initialize_llm` and `initialize_embeddings` functions in the `components/llm.py` file to set up the desired language and embedding models.

2. **Set Logging Level:**
   - Update logging configurations in the `app.py` file for debugging or production.

---

## Running the Application

1. **Start the Streamlit Server:**
   ```bash
   streamlit run app.py
   ```
2. **Access the Application:**
   - Open the application in your web browser at `http://localhost:8501`.

3. **Deployed Version:**
   - The application is also deployed at [https://queryassistant.streamlit.app/](https://queryassistant.streamlit.app/).

---

## Usage Instructions

### 1. Upload Documents
- Click the "Upload PDF files" button to select one or more PDF files.
- Wait for the files to process before querying.

### 2. Enter Financial Queries
- Use the input box to enter specific queries, such as:
  - *"What is the net profit in segment reporting?"*
  - *"Summarize operating expenses for Q1."*

### 3. View Results
- Responses are displayed below the query box with relevant document excerpts.

---

## Example Queries

1. *"What is the revenue for the last quarter?"*
2. *"List the operating costs for the fiscal year."*
3. *"Provide details of net income from the uploaded documents."*

---

## Key Components

### 1. **Frontend**
- Built using Streamlit for an intuitive user experience.
- Features include document upload, query input, and response display.

### 2. **Backend**
- **Document Processing:** Extracts tables and text from PDFs using pdfplumber.
- **Indexing:** Indexes financial data with llama_index for efficient retrieval.
- **Embeddings:** Uses HuggingFace embeddings for similarity-based searches.
- **LLM Integration:** Answers queries using Gemini-1.5-flash.

---

## Contribution

1. Fork the repository.
2. Create a feature branch.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch.
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---




