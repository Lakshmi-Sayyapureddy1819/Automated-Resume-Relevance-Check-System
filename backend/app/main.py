from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Automated Resume Relevance Check")

app.include_router(api_router, prefix="/api")

@app.get("/")
async def health_check():
    return {"status": "Running"}
