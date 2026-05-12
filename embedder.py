import os
import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed(self, chunks):
        vectors = self.model.encode(chunks)
        return [np.array(v).flatten().tolist() for v in vectors]

    def embed_q(self, query):
        v = self.model.encode(query)
        return np.array(v).flatten().tolist()
