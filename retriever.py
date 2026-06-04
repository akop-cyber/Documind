import numpy as np
import re

class Retriever:
    def __init__(self, vector_store, embedder,bm25, k=3,threshold = 0.4):
        self.vector_store = vector_store
        self.embedder = embedder
        self.k = k
        self.threshold = threshold
        self.bm25 = bm25

    def retrieve(self, query):
        mquery = query    
        
        vquery = self.embedder.embed_q(mquery)
        query_tokens = re.findall(r"\w+", mquery.lower())


        
        faiss_scores, faiss_indices = self.vector_store.search(vquery, self.k)

        bm25_scores = self.bm25.get_scores(query_tokens)
        bm25_indices = np.argsort(bm25_scores)[::-1][:self.k]
        bm25_top_scores = bm25_scores[bm25_indices]

        def normalise(scores):
            mn = min(scores)
            mx = max(scores)
            return [(s - mn)/(mx - mn + 1e-8) for s in scores]
        

        faiss_norm = np.array(normalise(faiss_scores))
        bm25_norm = np.array(normalise(bm25_top_scores))

        faiss_dict = {
            idx : score
            for idx , score in zip(faiss_indices,faiss_norm)
        }

        bm25_dict = {
            idx : score
            for idx, score in zip(bm25_indices,bm25_norm)
        }


        candidates = set(faiss_indices.tolist() + bm25_indices.tolist())

        final = []

        for idx in candidates:
            faiss = faiss_dict.get(idx,0)
            bm25 = bm25_dict.get(idx,0)
            avg = (faiss + bm25)/2
            final.append((idx,avg))

        final.sort(
            key= lambda x: x[1],
            reverse= True
        )

        top_indices = [
            idx
            for idx , scores in final[:self.k]
        ]

        
        if final[0][1] < self.threshold:
            print(f"Evidence too low: {final[0]}")
            return []

        
        results = [
            self.vector_store.chunks[i] 
            for i in top_indices if i != -1
        ]
        return results




