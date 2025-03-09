from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

document_vectors = None
model = SentenceTransformer("all-MiniLM-L6-v2")


def store_document_vectors(text):
    global document_vectors
    sentences = text.split(". ")
    embeddings = model.encode(sentences)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    document_vectors = (index, sentences)

def load_vector_store():
    if document_vectors is None:
        raise RuntimeError("No document vectors found. Please upload a document first.")
    return document_vectors
