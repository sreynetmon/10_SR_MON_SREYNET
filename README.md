# Baseline Chat-with-Documents

A minimal, hands-on **Retrieval-Augmented Generation (RAG)** application built with Python, Ollama, and ChromaDB.

This project implements a local **Naive RAG pipeline** that loads documents, splits them into chunks, creates embeddings, stores them in ChromaDB, retrieves relevant chunks, and generates answers using a local LLM.

---

## 1. What is RAG?

**RAG (Retrieval-Augmented Generation)** is a technique that allows an LLM to answer questions using information from external documents.

Instead of relying only on the knowledge already learned by the LLM, RAG retrieves relevant information from documents and provides it to the LLM as context.

The pipeline is:

```text
Documents
    |
    v
Ingestion
    |
    v
Chunking
    |
    v
Embeddings
    |
    v
ChromaDB
    |
    v
Retrieval
    |
    v
Local LLM
    |
    v
Answer

--

## 2. Project Structure
chat-with-document-app/
│
├── app/
│   ├── chunking.py
│   ├── config.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── ingestion.py
│   ├── main.py
│   ├── pipeline.py
│   ├── retriever.py
│   └── vector_store.py
│
├── data/
│   ├── document1.txt
│   ├── document2.txt
│   ├── document3.txt
│   └── ...
│
├── README.md
├── reflection.md
├── .gitignore
├── pyproject.toml
└── poetry.lock

--

## 3. Prerequisites

1. Ollama (local LLM server)
Ollama runs LLMs locally on your machine. Install it from ollama.com, then pull the two models this app needs:

ollama pull nomic-embed-text   # embedding model (Stage 2 & 3)
ollama pull qwen3:8b           # generation model (Stage 4)
Verify Ollama is running:

ollama list   # should show both models
2. Poetry (Python package manager)
Poetry manages Python dependencies cleanly. Install it once:

pipx install poetry

Setup
cd rag-baseline-app
poetry install 

--

## 4. Chunking Strategy

The project uses:

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120

A chunk size of 800 characters keeps each retrieved section focused while
still providing enough context for the LLM.

A 120-character overlap helps preserve context between neighboring chunks
and reduces the chance of losing information when an important sentence or
idea crosses a chunk boundary.