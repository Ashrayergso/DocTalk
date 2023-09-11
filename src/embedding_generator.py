```python
import numpy as np
from lib.langchain import Langchain

class EmbeddingGenerator:
    def __init__(self):
        self.langchain = Langchain()

    def generate_embeddings(self, text_chunks):
        embeddings = []
        for chunk in text_chunks:
            embedding = self.langchain.generate_embedding(chunk)
            embeddings.append(embedding)
        return np.array(embeddings)
```