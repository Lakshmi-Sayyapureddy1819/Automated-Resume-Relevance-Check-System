def extract_must_have_keywords(jd_text: str) -> list:
    # Placeholder: For now, hardcoded or simple regex-based extraction
    # Ideally, use spaCy or keyword extraction for must-have skills
    return ["python", "machine learning", "nlp", "data science", "sql"]

def compute_keyword_match_score(resume_text: str, keywords: list) -> float:
    resume_words = set(resume_text.lower().split())
    hits = sum(1 for kw in keywords if kw in resume_words)
    if not keywords:
        return 0.0
    return hits / len(keywords) * 50  # max score 50
