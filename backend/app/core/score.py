from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def semantic_similarity_score(jd_embedding: np.array, resume_embedding: np.array) -> float:
    similarity = cosine_similarity([jd_embedding], [resume_embedding])[0][0]
    return similarity * 50  # max score 50

def combined_score(hard_score: float, semantic_score: float, weights=(0.5,0.5)) -> float:
    return weights[0]*hard_score + weights[1]*semantic_score
