from typing import List

import ollama

from app.config import GEN_MODEL, SYSTEM_PROMPT
from app.retriever import RetrievedChunk


def build_prompt(
    query: str,
    chunks: List[RetrievedChunk],
) -> str:

    if not chunks:
        context_block = "(no relevant context was found)"

    else:
        context_block = "\n\n".join(
            f"[{i + 1}] Source: {chunk['source']}\n"
            f"{chunk['text']}"
            for i, chunk in enumerate(chunks)
        )

    return (
        f"Context:\n{context_block}\n\n"
        f"Question: {query}\n\n"
        "Answer using only the context above. "
        "If the answer is not contained in the context, "
        "say: I don't have enough information in the documents "
        "to answer that."
    )


def generate_answer(
    query: str,
    chunks: List[RetrievedChunk],
) -> str:

    prompt = build_prompt(
        query,
        chunks,
    )

    response = ollama.chat(
        model=GEN_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.message.content
