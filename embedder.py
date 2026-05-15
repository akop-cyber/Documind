import numpy as np
import os
from huggingface_hub import InferenceClient

class Embedder:
    def __init__(self):
        self.client = InferenceClient(token=os.environ["HF_TOKEN"])
        self.model = "BAAI/bge-small-en-v1.5"

    def embed(self, chunks, batch_size=32):
        all_vectors = []

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]

            try:
                batch_vectors = self.client.feature_extraction(
                    batch,
                    model=self.model
                )

                all_vectors.extend(batch_vectors)

            except Exception as e:
                print(f"Embedding batch failed: {e}")
                raise e

        return all_vectors

    def embed_q(self, query):
        v = self.client.feature_extraction(
            query,
            model=self.model
        )
        return np.array(v).tolist()
