def retrieve_relevant_passages(query, vector_store):
    index, sentences = vector_store
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=3)
    return [sentences[i] for i in I[0] if i < len(sentences)]
