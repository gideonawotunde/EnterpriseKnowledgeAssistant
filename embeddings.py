import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the environment.")

client = genai.Client(api_key=api_key)

EMBEDDING_MODEL = "gemini-embedding-001"


def create_embeddings(chunks):
    embeddings = []

    for chunk in chunks:
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=chunk
        )

        embeddings.append(response.embeddings[0].values)

    return embeddings
if __name__ == "__main__":
    test_chunks = [
        "Employees receive 25 vacation days per year.",
        "Python is a popular programming language.",
        "Machine learning allows computers to learn from data."
    ]

    embeddings = create_embeddings(test_chunks)

    print(f"Created {len(embeddings)} embeddings.")
    print(f"Dimensions: {len(embeddings[0])}")
    print(f"First embedding length: {len(embeddings[0])}")