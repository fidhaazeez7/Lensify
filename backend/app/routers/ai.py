from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import ask_ai

router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    analysis: dict
    bugs: list
    security: list
    health: dict
    performance: dict
    documentation: dict
    architecture: dict
    technology: dict

@router.post("/chat")
async def chat(request: ChatRequest):
    answer = ask_ai(
    question=request.question,
    analysis=request.analysis,
    bugs=request.bugs,
    security=request.security,
    health=request.health,
    performance=request.performance,
    documentation=request.documentation,
    architecture=request.architecture,
    technology=request.technology,
)
    

    return {
        "answer": answer
    }