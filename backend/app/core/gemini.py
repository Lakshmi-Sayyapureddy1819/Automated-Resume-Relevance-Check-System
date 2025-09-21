import os
import requests
import numpy as np

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_EMBED_URL = "https://api.gemini.ai/v1/embeddings"  # Adjust according to actual docs

def get_gemini_embedding(text: str) -> np.array:
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"input": text, "model": "gemini-embedding-001"}
    response = requests.post(GEMINI_EMBED_URL, json=payload, headers=headers)
    response.raise_for_status()
    embedding = response.json()["data"][0]["embedding"]
    return np.array(embedding)
