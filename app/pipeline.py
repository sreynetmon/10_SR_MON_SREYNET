from app.chunking import chunk_text
from app.embeddings import embed_texts
from app.generator import generate_answer
from app.ingestion import load_documents
from app.retriever import retrieve
from app.vector_store import add_chunks, reset_collection


def build_index() -> int:

    documents = load_documents()

    if not documents:
        raise FileNotFoundError(
            "No documents found in data/"
        )

    ids = []
    texts = []
    metadatas = []

    for filename, full_text in documents:

        chunks = chunk_text(full_text)

        for chunk_index, chunk in enumerate(chunks):

            ids.append(
                f"{filename}::{chunk_index}"
            )

            texts.append(chunk)

            metadatas.append(
                {
                    "source": filename,
                    "chunk_index": chunk_index,
                }
            )

    embeddings = embed_texts(texts)

    reset_collection()

    add_chunks(
        ids=ids,
        texts=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return len(texts)


def ask_question(
    question: str,
    top_k: int = 4,
):

    chunks = retrieve(
        question,
        top_k,
    )

    answer = generate_answer(
        question,
        chunks,
    )

    return answer, chunks
