```python
import numpy as np
from lib import faiss

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        self.index.add(np.array(embeddings, dtype=np.float32))

    def search(self, query_embedding, k=10):
        distances, indices = self.index.search(np.array([query_embedding], dtype=np.float32), k)
        return distances[0], indices[0]
```