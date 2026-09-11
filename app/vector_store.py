import chromadb
from chromadb.config import Settings

from app.config import CHROMA_DB_DIR, COLLECTION_NAME


def get_client():
    """
    Create and return the persistent ChromaDB client.
    """

    return chromadb.PersistentClient(
        path=CHROMA_DB_DIR,
        settings=Settings(
            anonymized_telemetry=False
        ),
    )


def get_collection():
    """
    Get or create the document collection.
    """

    client = get_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def reset_collection():
    """
    Delete the existing collection and create a new one.
    """

    client = get_client()

    try:
        client.delete_collection(
            COLLECTION_NAME
        )
    except Exception:
        pass

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def add_chunks(
    ids: list[str],
    texts: list[str],
    embeddings: list[list[float]],
    metadatas: list[dict],
):
    """
    Add document chunks and their embeddings to ChromaDB.
    """

    collection = get_collection()

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search(
    query_embedding: list[float],
    top_k: int = 3,
):
    """
    Search ChromaDB using a query embedding.
    """

    collection = get_collection()

    if collection.count() == 0:
        return {
            "documents": [[]],
            "metadatas": [[]],
            "distances": [[]],
        }

    top_k = min(
        top_k,
        collection.count(),
    )

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )


def count() -> int:
    """
    Return the number of stored chunks.
    """

    return get_collection().count()
