import os
from app.services.framework_detector import detect_frameworks


def has_folder(folders: set, *names):
    """Check if any folder exists."""
    return any(name.lower() in folders for name in names)


def has_file(files: set, *names):
    """Check if any file exists."""
    return any(name.lower() in files for name in names)


def detect_architecture(folder_path: str):

    folders = set()
    files = set()

    # Scan project structure
    for root, dirs, filenames in os.walk(folder_path):

        # Ignore hidden folders
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for d in dirs:
            folders.add(d.lower())

        for f in filenames:
            files.add(f.lower())

    # Detect frameworks
    frameworks = detect_frameworks(folder_path)

    frontend = frameworks.get("frontend")
    backend = frameworks.get("backend")
    database = frameworks.get("database")
    deployment = frameworks.get("deployment")

    architecture = "Unknown"
    pattern = "Unknown"
    confidence = 0

    # =====================================================
    # 1. MERN Stack
    # =====================================================

    if (
        frontend == "React"
        and backend == "Express.js"
        and database == "MongoDB"
    ):

        architecture = "MERN Stack"
        pattern = "React → Express → MongoDB"
        confidence = 98
         # =====================================================
    # 2. MEAN Stack
    # =====================================================

    elif (
        frontend == "Angular"
        and backend == "Express.js"
        and database == "MongoDB"
    ):

        architecture = "MEAN Stack"
        pattern = "Angular → Express → MongoDB"
        confidence = 98

    # =====================================================
    # 3. Clean Architecture
    # =====================================================

    elif (
        has_folder(folders, "domain")
        and has_folder(folders, "usecases", "use_cases", "application")
        and has_folder(folders, "repositories", "repository")
    ):

        architecture = "Clean Architecture"
        pattern = "Domain → Use Cases → Repository"
        confidence = 95

    # =====================================================
    # 4. Hexagonal Architecture
    # =====================================================

    elif (
        has_folder(folders, "ports")
        and has_folder(folders, "adapters")
    ):

        architecture = "Hexagonal Architecture"
        pattern = "Ports → Adapters"
        confidence = 95

    # =====================================================
    # 5. Spring Layered Architecture
    # =====================================================

    elif (
        backend == "Spring Boot"
        and has_folder(folders, "controller", "controllers")
        and has_folder(folders, "service", "services")
        and has_folder(folders, "repository", "repositories")
    ):

        architecture = "Spring Layered Architecture"
        pattern = "Controller → Service → Repository"
        confidence = 97

    # =====================================================
    # 6. FastAPI Layered Architecture
    # =====================================================

    elif (
        backend == "FastAPI"
        and (
            has_folder(folders, "router", "routers")
            or has_folder(folders, "controller", "controllers")
        )
        and has_folder(folders, "service", "services")
    ):

        architecture = "FastAPI Layered Architecture"

        if has_folder(folders, "repository", "repositories"):
            pattern = "Router → Service → Repository"
        elif database:
            pattern = f"Router → Service → {database}"
        else:
            pattern = "Router → Service"

        confidence = 95

    # =====================================================
    # 7. Flask MVC
    # =====================================================

    elif (
        backend == "Flask"
        and has_folder(folders, "templates")
    ):

        architecture = "Flask MVC"
        pattern = "Model → View → Controller"
        confidence = 94

    # =====================================================
    # 8. Django MVC
    # =====================================================

    elif has_file(files, "manage.py"):

        architecture = "Django MVC"
        pattern = "Model → View → Template"
        confidence = 95  
        # =====================================================
    # 9. Layered Architecture (Generic)
    # =====================================================

    elif (
        (
            has_folder(folders, "controller", "controllers")
            or has_folder(folders, "router", "routers")
        )
        and has_folder(folders, "service", "services")
        and (
            has_folder(folders, "repository", "repositories")
            or has_folder(folders, "dao")
            or database
        )
    ):

        architecture = "Layered Architecture"

        if has_folder(folders, "repository", "repositories"):
            pattern = "Controller → Service → Repository"
        elif database:
            pattern = f"Controller → Service → {database}"
        else:
            pattern = "Controller → Service"

        confidence = 90

    # =====================================================
    # 10. REST API
    # =====================================================

    elif backend in [
        "FastAPI",
        "Flask",
        "Django",
        "Express.js",
        "Spring Boot",
        "ASP.NET",
        "NestJS",
        "Laravel",
    ]:

        architecture = "REST API"
        pattern = f"{backend} REST API"
        confidence = 85

    # =====================================================
    # 11. Client–Server
    # =====================================================

    elif frontend and backend:

        architecture = "Client–Server"

        if database:
            pattern = f"{frontend} → {backend} → {database}"
        else:
            pattern = f"{frontend} → {backend}"

        confidence = 88

    # =====================================================
    # 12. React Component Architecture
    # =====================================================

    elif (
        frontend == "React"
        and has_folder(folders, "components")
    ):

        architecture = "Component-Based Architecture"
        pattern = "Reusable React Components"
        confidence = 82

    # =====================================================
    # 13. Serverless
    # =====================================================

    elif has_file(
        files,
        "serverless.yml",
        "serverless.yaml",
        "template.yaml",
        "template.yml",
    ):

        architecture = "Serverless"
        pattern = "Cloud Functions"
        confidence = 92

    # =====================================================
    # 14. Event-Driven
    # =====================================================

    elif (
        has_folder(folders, "events")
        or has_folder(folders, "listeners")
        or has_folder(folders, "consumers")
        or has_folder(folders, "producers")
    ):

        architecture = "Event-Driven Architecture"
        pattern = "Publish → Event Bus → Subscriber"
        confidence = 90

    # =====================================================
    # 15. Microservices
    # =====================================================

    elif (
        has_file(files, "docker-compose.yml", "docker-compose.yaml")
        and has_folder(folders, "services")
        and len(folders) >= 8
    ):

        architecture = "Microservices"
        pattern = "Independent Containerized Services"
        confidence = 80

    # =====================================================
    # 16. Monolithic
    # =====================================================

    elif len(files) > 20:

        architecture = "Monolithic"
        pattern = "Single Deployable Application"
        confidence = 75  
        # =====================================================
    # Deployment Information
    # =====================================================

    indicators = []

    if frontend:
        indicators.append(frontend)

    if backend:
        indicators.append(backend)

    if database:
        indicators.append(database)

    if deployment:
        indicators.append(deployment)

    architecture_map = {
        "controller": "controller/",
        "controllers": "controllers/",
        "router": "router/",
        "routers": "routers/",
        "service": "service/",
        "services": "services/",
        "repository": "repository/",
        "repositories": "repositories/",
        "dao": "dao/",
        "domain": "domain/",
        "usecases": "usecases/",
        "use_cases": "use_cases/",
        "application": "application/",
        "ports": "ports/",
        "adapters": "adapters/",
        "components": "components/",
        "templates": "templates/",
        "events": "events/",
        "listeners": "listeners/",
        "consumers": "consumers/",
        "producers": "producers/",
    }

    for folder, label in architecture_map.items():
        if folder in folders:
            indicators.append(label)

    if deployment:
        pattern += f" | Deployment: {deployment}"

    # Remove duplicate indicators while preserving order
    indicators = list(dict.fromkeys(indicators))

    return {
        "architecture": architecture,
        "pattern": pattern,
        "confidence": confidence,
        "frameworks": frameworks,
        "indicators": indicators,
    }      