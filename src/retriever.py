from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, documents):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = documents
        self.embeddings = self.model.encode(documents)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, k=2):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), k)

        results = [self.documents[i] for i in indices[0]]
        return results