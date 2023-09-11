```python
import numpy as np
import faiss

class FaissIndex:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors):
        self.index.add(np.array(vectors, dtype=np.float32))

    def search_vectors(self, vectors, k):
        return self.index.search(np.array(vectors, dtype=np.float32), k)
```