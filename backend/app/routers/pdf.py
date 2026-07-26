from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.services.pdf_service import generate_pdf

router = APIRouter()


class PDFRequest(BaseModel):
    analysis: dict
    technology: dict
    architecture: dict
    performance: dict
    documentation: dict
    ai_review: dict
    health: dict
    bugs: list
    security: list


@router.post("/download-report")
async def download_report(request: PDFRequest):

    pdf_path = generate_pdf(
        request.analysis,
        request.health,
        request.bugs,
        request.security,
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="Lensify_Report.pdf",
    )