# Chat with Documents

A local Retrieval-Augmented Generation (RAG) application that answers questions
about text documents using Ollama and ChromaDB.

## Overview

### What is RAG?

Retrieval-Augmented Generation (RAG) gives a language model relevant
information from external documents before it generates an answer. This
application uses a local RAG pipeline:

1. Load documents from `data/`.
2. Split the documents into overlapping chunks.
3. Create embeddings with Ollama.
4. Store the chunks and embeddings in ChromaDB.
5. Retrieve the most relevant chunks for a question.
6. Generate an answer with a local language model.

### Pipeline

```text
Documents -> Ingestion -> Chunking -> Embeddings -> ChromaDB
                                                        |
                                                        v
Question -> Retrieval -> Local LLM -> Answer
```

## Project Structure

```text
chat-with-document-app/
├── app/
│   ├── chunking.py       # Splits documents into overlapping chunks
│   ├── config.py         # Models and pipeline settings
│   ├── embeddings.py     # Creates document embeddings
│   ├── generator.py      # Generates answers with the local LLM
│   ├── ingestion.py      # Loads text documents
│   ├── main.py           # Command-line application entry point
│   ├── pipeline.py       # Builds the index and answers questions
│   ├── retriever.py      # Retrieves relevant document chunks
│   └── vector_store.py   # Stores and queries ChromaDB
├── data/                 # Source text documents
├── chroma_db/            # Local ChromaDB data
├── README.md
├── pyproject.toml
└── poetry.lock
```

## Requirements

### Python

- Python 3.14 or newer
- Poetry

### Ollama

Install [Ollama](https://ollama.com/) and make sure it is running. Pull the
models used by the application:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2:3b
```

Verify that both models are available:

```bash
ollama list
```

## Installation

Run these commands from the project root:

```bash
poetry install
```

## Usage

Start the interactive chat application with:

```bash
poetry run python -m app.main
```

The application builds an index from the files in `data/`, then prompts for
questions. Type `exit` to close the application.

## Configuration

The default settings are defined in `app/config.py`:

### Models

- Embedding model: `nomic-embed-text`
- Generation model: `llama3.2:3b`

### Chunking

- Chunk size: `800` characters
- Chunk overlap: `120` characters

### Retrieval

- Retrieved chunks per question: `4`

## Data

Place plain-text (`.txt`) documents in the `data/` directory. The index is
rebuilt when the application starts, and the generated ChromaDB data is stored
in `chroma_db/`.
