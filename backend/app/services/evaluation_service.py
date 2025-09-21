import asyncio
from app.core.parser import extract_text_from_pdf
from app.core.gemini import get_gemini_embedding
from app.core.keywords import extract_must_have_keywords, compute_keyword_match_score
from app.core.score import semantic_similarity_score, combined_score
from app.schemas import EvaluationResponse

async def evaluate_resume_job(job_desc_file, resume_file) -> EvaluationResponse:
    jd_text, resume_text = await asyncio.gather(
        extract_text_from_pdf(job_desc_file),
        extract_text_from_pdf(resume_file),
    )
    must_have_keywords = extract_must_have_keywords(jd_text)
    hard_score = compute_keyword_match_score(resume_text, must_have_keywords)

    jd_emb = get_gemini_embedding(jd_text)
    resume_emb = get_gemini_embedding(resume_text)
    semantic_score = semantic_similarity_score(jd_emb, resume_emb)

    final_score = combined_score(hard_score, semantic_score)

    if final_score >= 70:
        verdict = "High Suitability"
    elif final_score >= 40:
        verdict = "Medium Suitability"
    else:
        verdict = "Low Suitability"

    resume_words = set(resume_text.lower().split())
    missing_skills = [kw for kw in must_have_keywords if kw not in resume_words]

    suggestions = []
    if missing_skills:
        suggestions.append(f"Add missing skills: {', '.join(missing_skills)}")
    if semantic_score < 25:
        suggestions.append("Improve description relevance to job requirements")

    return EvaluationResponse(
        score=round(final_score, 2),
        verdict=verdict,
        missing_skills=missing_skills,
        suggestions=suggestions or ["Good fit!"]
    )
