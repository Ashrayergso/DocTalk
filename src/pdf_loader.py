```python
import os
from PyPDF2 import PdfFileReader
from lib.langchain import Langchain

class PDFLoader:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.langchain = Langchain()

    def load_pdfs(self):
        pdf_files = self._get_pdf_files()
        loaded_pdfs = [self._load_pdf(file) for file in pdf_files]
        return loaded_pdfs

    def _get_pdf_files(self):
        files = os.listdir(self.directory_path)
        pdf_files = [file for file in files if file.endswith('.pdf')]
        return pdf_files

    def _load_pdf(self, file):
        file_path = os.path.join(self.directory_path, file)
        with open(file_path, 'rb') as f:
            pdf = PdfFileReader(f)
            num_pages = pdf.getNumPages()
            text = [self.langchain.extract_text(pdf.getPage(i)) for i in range(num_pages)]
        return text
```