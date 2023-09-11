```python
from langchain import Langchain

class QueryProcessor:
    def __init__(self):
        self.langchain = Langchain()

    def process_query(self, user_query):
        processed_query = self.langchain.process_chat_query(user_query)
        return processed_query
```