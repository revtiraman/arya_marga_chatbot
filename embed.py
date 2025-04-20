import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load CSV
df = pd.read_csv("/Users/revtiramantripathi/Downloads/yoga_sutras_1000_detailed.csv")


# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert sutras to embeddings
embeddings = model.encode(df["sutra"].tolist())
embeddings = np.array(embeddings)

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save everything
faiss.write_index(index, "sutra_index.faiss")
df.to_pickle("sutras.pkl")
