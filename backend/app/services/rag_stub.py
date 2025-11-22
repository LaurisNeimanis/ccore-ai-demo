def rag_query(query: str):
    return {
        "query": query,
        "retrieved_context": [
            "This is a demo context chunk. In real systems this comes from vector DB."
        ],
        "answer": f"Stub RAG answer for: {query}"
    }
