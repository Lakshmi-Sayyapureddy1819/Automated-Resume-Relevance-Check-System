import google.generativeai as genai
import numpy as np
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def get_gemini_embedding(text: str) -> np.array:
    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="RETRIEVAL_DOCUMENT"
    )
    return np.array(result['embedding'])