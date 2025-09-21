import os
import google.generativeai as genai
import numpy as np

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_embedding(text: str) -> np.array:
    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="RETRIEVAL_DOCUMENT"
    )
    return np.array(result['embedding'])