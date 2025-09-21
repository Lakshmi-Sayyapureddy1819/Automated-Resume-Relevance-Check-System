import re

def clean_text(text: str) -> str:
    """Basic text cleaning: lowercasing, removing special characters, etc."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def fuzzy_contains(token_list, word, threshold=0.8):
    """
    Does a simple fuzzy check if 'word' closely matches any token in 'token_list'.
    Use a basic measure (Jaccard or Levenshtein if available).
    """
    try:
        from difflib import SequenceMatcher
    except ImportError:
        return False
    for token in token_list:
        ratio = SequenceMatcher(None, token, word).ratio()
        if ratio >= threshold:
            return True
    return False

def extract_emails(text: str):
    """Extract emails from a block of text."""
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)
