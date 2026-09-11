from app.retriever import retrieve
from app.vector_store import count


def main():
    print("=" * 60)
    print("VECTOR DATABASE CHECK")
    print("=" * 60)

    print(f"Total chunks in ChromaDB: {count()}")

    question = input("\nEnter a test question: ").strip()

    if not question:
        print("Question cannot be empty.")
        return

    chunks = retrieve(question, top_k=3)

    print("\n" + "=" * 60)
    print("TOP 3 RETRIEVED CHUNKS")
    print("=" * 60)

    for index, chunk in enumerate(chunks, start=1):

        print(f"\n--- Result {index} ---")

        print(f"Source: {chunk['source']}")
        print(f"Chunk index: {chunk['chunk_index']}")
        print(f"Distance: {chunk['distance']}")

        print("\nText:")
        print(chunk["text"])


if __name__ == "__main__":
    main()
