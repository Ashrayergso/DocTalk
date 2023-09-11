```python
from llamacpp import LLM

class LLMModel:
    def __init__(self, model_path):
        self.model = LLM(model_path)

    def get_model(self):
        return self.model
```