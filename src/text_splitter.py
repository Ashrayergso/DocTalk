```python
import os
from langchain import TextChunker

class TextSplitter:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.text_chunker = TextChunker()

    def get_text_chunks(self):
        text_chunks = []
        for filename in os.listdir(self.directory_path):
            if filename.endswith(".pdf"):
                with open(os.path.join(self.directory_path, filename), 'r') as file:
                    document_text = file.read()
                    chunks = self.text_chunker.chunk_text(document_text)
                    text_chunks.extend(chunks)
        return text_chunks
```