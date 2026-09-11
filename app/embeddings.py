import ollama

from app.config import EMBED_MODEL


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple texts.
    """

    if not texts:
        return []

    response = ollama.embed(
        model=EMBED_MODEL,
        input=texts,
    )

    return list(response.embeddings)


def embed_query(query: str) -> list[float]:
    """
    Generate an embedding for a single query.
    """

    embeddings = embed_texts([query])

    return embeddings[0]
