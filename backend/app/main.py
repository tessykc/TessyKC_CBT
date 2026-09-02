from fastapi import FastAPI

from app.api.v1 import api_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description=(
        "Backend API for the Nigerian Secondary School "
        "CBT and Examination Preparation Platform."
    ),
)


app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/", tags=["System"])
def root():
    return {
        "message": "CBT Examination",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
    }