from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.services.pdf_service import generate_report


router = APIRouter()


class PDFRequest(BaseModel):
    analysis: dict
    health: dict
    bugs: list
    security: list


@router.post("/download-report")
async def download_report(request: PDFRequest):
    pdf = generate_report(request.model_dump())

    filename = (
        request.analysis.get("project_name", "lensify_report")
        + "_report.pdf"
    )

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        },
    )