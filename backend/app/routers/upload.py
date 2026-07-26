from typing import List

from fastapi import APIRouter, UploadFile, File

from app.services.file_service import save_and_extract_zip
from app.services.folder_service import save_uploaded_folder
from app.services.analyzer import analyze_project
from app.services.technology_detector import detect_technology
from app.services.architecture_analyzer import detect_architecture
from app.services.security_scanner import scan_security
from app.services.bug_scanner import scan_bugs
from app.services.health import calculate_health
from app.services.ai_review_service import generate_project_review
from app.services.performance_analyzer import analyze_performance
from app.services.documentation_analyzer import analyze_documentation

router = APIRouter()


# --------------------------------------------------
# ZIP Upload Endpoint
# --------------------------------------------------
@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    folder = save_and_extract_zip(file)

    # Project Analysis
    analysis = analyze_project(folder)

    # Technology Detection
    technology = detect_technology(folder)

    # Architecture Detection
    architecture = detect_architecture(folder)

    # Security Scan
    security = scan_security(folder)

    # Bug Detection
    bugs = scan_bugs(folder)

    # Health Score
    health = calculate_health(
        analysis,
        bugs,
        security,
    )

    # AI Review
    ai_review = generate_project_review(
        analysis,
        bugs,
        security,
        health,
    )


        # Performance Analysis
    performance = analyze_performance(folder)

    documentation = analyze_documentation(folder)

    # Debug Logs
    print("\n========== ANALYSIS ==========")
    print(analysis)

    print("\n========== TECHNOLOGY ==========")
    print(technology)

    print("\n========== ARCHITECTURE ==========")
    print(architecture)

    print("\n========== SECURITY ==========")
    print(security)

    print("\n========== BUGS ==========")
    print(bugs)

    print("==============================\n")

    return {
    "message": "ZIP analysis completed successfully",
    "analysis": analysis,
    "technology": technology,
    "architecture": architecture,
    "security": security,
    "bugs": bugs,
    "health": health,
    "ai_review": ai_review,
    "performance": performance,
}


# --------------------------------------------------
# Folder Upload Endpoint
# --------------------------------------------------
@router.post("/analyze-folder")
async def analyze_folder(
    files: List[UploadFile] = File(...)
):
    folder = save_uploaded_folder(files)

    # Project Analysis
    analysis = analyze_project(folder)

    # Technology Detection
    technology = detect_technology(folder)

    # Architecture Detection
    architecture = detect_architecture(folder)

    # Security Scan
    security = scan_security(folder)

    # Bug Detection
    bugs = scan_bugs(folder)

    # Health Score
    health = calculate_health(
        analysis,
        bugs,
        security,
    )

    # AI Review
    ai_review = generate_project_review(
        analysis,
        bugs,
        security,
        health,
    )

    performance = analyze_performance(folder)
    documentation = analyze_documentation(folder)

    # Debug Logs
    print("\n========== ANALYSIS ==========")
    print(analysis)

    print("\n========== TECHNOLOGY ==========")
    print(technology)

    print("\n========== ARCHITECTURE ==========")
    print(architecture)

    print("\n========== SECURITY ==========")
    print(security)

    print("\n========== BUGS ==========")
    print(bugs)

    print("==============================\n")

    return {
        "message": "Folder analysis completed successfully",
        "analysis": analysis,
        "technology": technology,
        "architecture": architecture,
        "security": security,
        "bugs": bugs,
        "health": health,
        "ai_review": ai_review,
        "performance": performance,
        "documentation": documentation,
    }