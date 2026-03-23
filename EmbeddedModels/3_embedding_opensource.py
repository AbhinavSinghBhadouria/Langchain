from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "delhi is the capital of india"

vector = embedding.embed_query(text)

print("Query embedding:")
print(f"Length: {len(vector)}")
print(f"First 10 values: {vector[:10]}")

documents = [
    "Delhi is the capital of India",
    "India is a diverse country",
    "Mumbai is the financial capital"
]

doc_vectors = embedding.embed_documents(documents)

print("\nDocument embeddings:")
for i, vec in enumerate(doc_vectors):
    print(f"Doc {i+1} length: {len(vec)}, first 5: {vec[:5]}")