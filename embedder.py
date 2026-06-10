import os
import time
import numpy as np
from huggingface_hub import InferenceClient

class Embedder:
    def __init__(self):
        self.client = InferenceClient(token=os.environ["HF_TOKEN"])
       
        self.model = "BAAI/bge-m3"

    def embed(self, chunks, batch_size=16): 
        all_vectors = []

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]

            try:
              
                response = self.client.feature_extraction(
                    batch,
                    model=self.model
                )
                
               
                batch_vectors = np.array(response).tolist()
                
               
                if len(np.shape(batch_vectors)) == 3:
                    batch_vectors = batch_vectors[0]

                all_vectors.extend(batch_vectors)
                
                
                time.sleep(0.5)

            except Exception as e:
               
                if "503" in str(e) or "loading" in str(e).lower():
                    print("Model is initializing on Hugging Face servers. Waiting 20 seconds...")
                    time.sleep(20)
                
                    return self.embed(chunks[i:], batch_size=batch_size)
                else:
                    print(f"Embedding batch failed: {e}")
                    raise e

        return all_vectors

    def embed_q(self, query):
        try:
            v = self.client.feature_extraction(
                query,
                model=self.model
            )
           
            return np.array(v).flatten().tolist()
        except Exception as e:
            if "503" in str(e):
                print("Model loading. Retrying query embedding in 15 seconds...")
                time.sleep(15)
                return self.embed_q(query)
            raise e

