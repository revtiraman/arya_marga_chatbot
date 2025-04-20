import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load saved files
df = pd.read_pickle("sutras.pkl")
index = faiss.read_index("sutra_index.faiss")
model = SentenceTransformer("all-MiniLM-L6-v2")

def search_sutra(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=1)
    match = df.iloc[I[0][0]]
    return {
        "sutra": match['sutra'],
        "explanation": match['explanation'],
        "resources": match['resources']
    }
