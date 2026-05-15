import os
import numpy as np
from huggingface_hub import InferenceClient

class Embedder:
    def __init__(self):
        self.client = InferenceClient(token=os.environ["HF_TOKEN"])
        self.model = "BAAI/bge-small-en-v1.5"

    def embed(self, chunks):
        vectors = [self.client.feature_extraction(chunks, model=self.model,batch_size = 32)]
        return [np.array(v).flatten().tolist() for v in vectors]

    def embed_q(self, query):
        v = self.client.feature_extraction(query, model=self.model)
        return np.array(v).flatten().tolist()
