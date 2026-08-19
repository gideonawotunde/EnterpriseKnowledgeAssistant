import chromadb


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="enterprise_documents"
)


def store_chunks(chunks, embeddings):
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

def search_chunks(query_embedding, n_results=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results

# if __name__ == "__main__":
#
#     test_chunks = [
#         "Employees receive 25 vacation days per year.",
#         "Python is a popular programming language.",
#         "The company supports remote work."
#     ]
#
#     test_embeddings = [
#         [0.1, 0.2, 0.3],
#         [0.4, 0.5, 0.6],
#         [0.7, 0.8, 0.9]
#     ]
#
#     store_chunks(test_chunks, test_embeddings)