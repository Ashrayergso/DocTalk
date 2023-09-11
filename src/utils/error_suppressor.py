```python
import os
import sys

def suppress_errors():
    sys.stderr = open(os.devnull, 'w')

def suppress_output():
    sys.stdout = open(os.devnull, 'w')

def restore_errors():
    sys.stderr = sys.__stderr__

def restore_output():
    sys.stdout = sys.__stdout__
```