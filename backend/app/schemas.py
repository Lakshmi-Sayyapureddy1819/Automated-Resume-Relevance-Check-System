from pydantic import BaseModel
from typing import List

class EvaluationResponse(BaseModel):
    score: float
    verdict: str
    missing_skills: List[str]
    suggestions: List[str]
