from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.upload import router as upload_router
from app.routers.ai import router as ai_router
from app.routers.report import router as report_router

app = FastAPI(
    title="Lensify API",
    version="1.0.0",
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://lensify-ai.onrender.com",   
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Lensify Backend Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


app.include_router(upload_router)
app.include_router(ai_router)
app.include_router(report_router)