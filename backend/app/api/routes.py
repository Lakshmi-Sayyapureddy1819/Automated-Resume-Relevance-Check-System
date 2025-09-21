from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.evaluation_service import evaluate_resume_job
from app.schemas import EvaluationResponse

router = APIRouter()

@router.post("/evaluate/", response_model=EvaluationResponse)
async def evaluate(job_description: UploadFile = File(...), resume: UploadFile = File(...)):
    if job_description.content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Job Description must be PDF")
    if resume.content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Resume must be PDF")
    result = await evaluate_resume_job(job_description, resume)
    return result
