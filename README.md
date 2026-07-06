# RAG Product Development 🤖📋

**Retrieval-Augmented Generation chatbot for product development knowledge retrieval.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

---

## Overview

A RAG (Retrieval-Augmented Generation) chatbot that answers questions about product development methodology. Built with:

- **LangChain** — orchestration framework
- **Chroma DB** — vector database for document retrieval
- **OpenAI LLM** — natural language responses
- **NLTK** — text preprocessing

The system ingests product development documents, indexes them into a vector database, and answers user queries by retrieving relevant context and generating responses with an LLM.

---

## How It Works

```
Documents → Chunking → Embeddings → Chroma DB
                                            ↓
User Query → Retrieve relevant chunks → LLM → Answer
```

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up your API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Download NLTK data
python nltk_download.py

# Build the vector database
python create_database.py

# Run the chatbot
python produkt_entwickulng_bot.py
```

---

## Files

| File | Purpose |
|------|---------|
| `produkt_entwickulng_bot.py` | Main chatbot application |
| `create_database.py` | Builds Chroma DB from source documents |
| `Word_to_json.py` | Converts Word documents to JSON |
| `nltk_download.py` | Downloads NLTK resources |
| `requirements.txt` | Python dependencies |

---

## License

MIT
