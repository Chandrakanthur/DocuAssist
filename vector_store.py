from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

document_vectors = None
model = SentenceTransformer("all-MiniLM-L6-v2")
