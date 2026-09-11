from app.pipeline import build_index, ask_question


def main():
    print("=" * 60)
    print("        Local RAG - Chat with Documents")
    print("=" * 60)

    print("\nBuilding document index...")

    try:
        chunk_count = build_index()
        print(f"Indexed {chunk_count} chunks successfully.")

    except Exception as error:
        print(f"\nError building index: {error}")
        return

    print("\nYour documents are ready.")
    print("Ask questions about your documents.")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        try:
            answer, chunks = ask_question(
                question,
                top_k=4,
            )

            print("\n" + "-" * 60)
            print("Retrieved Chunks")
            print("-" * 60)

            for index, chunk in enumerate(chunks, start=1):
                print(f"\n--- Chunk {index} ---")
                print(f"Source: {chunk['source']}")
                print(f"Chunk index: {chunk['chunk_index']}")
                print(f"Distance: {chunk['distance']}")
                print("\nText:")
                print(chunk["text"])

            print("\n" + "-" * 60)
            print("Answer")
            print("-" * 60)
            print(answer)

        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
