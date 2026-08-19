import os

from dotenv import load_dotenv
from google import genai

from embeddings import create_embeddings
from vector_store import search_chunks

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the environment.")

client = genai.Client(api_key=api_key)

def main():

    question = input("Enter your question: ")

    print("\nCreating question embedding...")

    question_embedding = create_embeddings([question])[0]

    print("Searching ChromaDB...")

    results = search_chunks(question_embedding, n_results=5)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    RELEVANCE_THRESHOLD = 0.7

    if distances[0] > RELEVANCE_THRESHOLD:
        print("\nI could not find relevant information in the document.")
        return

    relevant_documents = []
    relevant_metadatas = []
    relevant_distances = []

    for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
    ):
        if distance <= RELEVANCE_THRESHOLD:
            relevant_documents.append(document)
            relevant_metadatas.append(metadata)
            relevant_distances.append(distance)

    sources = []
    context_parts = []

    for document, metadata, distance in zip(relevant_documents, relevant_metadatas, relevant_distances):
        document_name = metadata["document"]
        chunk_number = metadata["chunk"]

        sources.append(
            f"{document_name} — Chunk {chunk_number}"
        )

        context_parts.append(
            f"""--- Source: {document_name} | Chunk: {chunk_number} ---

    {document}"""
        )
        print(
            f"Retrieved: {document_name} |" 
            f"Chunk: {chunk_number} |" 
            f"Distance: {distance:.4f}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an enterprise document assistant.

Answer the user's question using ONLY the information
provided in the document context below.

If the answer cannot be found in the context, say:
"I could not find that information in the document."

Do not make up information.

Document context:
{context}

User question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        print("\nAnswer:\n")
        print(response.text)

    except Exception as e:
        print("\nUnable to generate an answer right now.")
        print("Please try again in a moment.")
        print(f"\nError: {e}")
        return

    print("\nSources:")

    for source in sources:
        print(f"- {source}")


if __name__ == "__main__":
    main()