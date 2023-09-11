```python
import os
from src.pdf_loader import load_pdfs
from src.text_splitter import split_text
from src.embedding_generator import generate_embeddings
from src.vector_store import store_vectors
from src.query_processor import process_query
from src.llm_retriever import retrieve_sections
from src.utils.error_suppressor import suppress_errors
from src.utils.infinite_loop import infinite_loop

# Suppress standard output and error
suppress_errors()

# Load PDF documents from a specified directory
directory_path = "/path/to/pdf/directory"
pdf_files = load_pdfs(directory_path)

# Split the loaded documents into smaller text chunks
text_chunks = split_text(pdf_files)

# Generate embeddings for each text chunk
embeddings = generate_embeddings(text_chunks)

# Store these embeddings in the FAISS vector store
store_vectors(embeddings)

# Enter into an infinite loop to await user queries
@infinite_loop
def await_queries():
    # Process the user queries
    query = input("Enter your query: ")
    processed_query = process_query(query)

    # Use llamacpp with a local llm model to retrieve the most relevant document sections
    relevant_sections = retrieve_sections(processed_query)

    print(relevant_sections)

# Start the application
if __name__ == "__main__":
    await_queries()
```