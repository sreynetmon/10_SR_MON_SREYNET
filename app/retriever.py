from typing import List, TypedDict

from app.config import TOP_K
from app.embeddings import embed_query
from app.vector_store import search


class RetrievedChunk(TypedDict):
    text: str
    source: str
    chunk_index: int
    distance: float


def retrieve(
    query: str,
    top_k: int = TOP_K,
) -> List[RetrievedChunk]:

    query_embedding = embed_query(query)

    results = search(
        query_embedding,
        top_k,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    chunks: List[RetrievedChunk] = []

    for text, meta, distance in zip(
        documents,
        metadatas,
        distances,
    ):
        chunks.append(
            {
                "text": text,
                "source": meta.get(
                    "source",
                    "unknown",
                ),
                "chunk_index": meta.get(
                    "chunk_index",
                    -1,
                ),
                "distance": distance,
            }
        )

    return chunks
