import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

class Settings:
    # API keys and sensitive data from .env
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyDAH3gZbmTJQJ_rN2EK1qHpBTUB-WdjTE8")
    # For real deployments, throw error if key is not present
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not set in environment variables or .env file.")
        
    GEMINI_EMBED_URL: str = os.getenv(
        "GEMINI_EMBED_URL",
        "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent"
    )

    # Add other configuration as needed
    # E.g., thresholds, file limits, DB URI etc.
    HARD_MATCH_WEIGHT: float = float(os.getenv("HARD_MATCH_WEIGHT", "0.5"))
    SEMANTIC_MATCH_WEIGHT: float = float(os.getenv("SEMANTIC_MATCH_WEIGHT", "0.5"))
    HIGH_THRESHOLD: int = int(os.getenv("HIGH_THRESHOLD", "70"))
    MEDIUM_THRESHOLD: int = int(os.getenv("MEDIUM_THRESHOLD", "40"))

settings = Settings()
