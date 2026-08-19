import chromadb


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="enterprise_documents"
)

def store_chunks(chunks, embeddings, document_name):

    ids = [
        f"{document_name}_chunk_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "document": document_name,
            "page": chunk["page"],
            "chunk": i
        }
        for i, chunk in enumerate(chunks)
    ]

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

def document_exists(document_name):
    results = collection.get(
        where={"document": document_name},
        limit=1
    )

    return len(results["ids"]) > 0

def delete_document(document_name):
    collection.delete(
        where={"document": document_name}
    )

    print(f"Removed existing chunks for {document_name}.")

def search_chunks(query_embedding, n_results=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
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