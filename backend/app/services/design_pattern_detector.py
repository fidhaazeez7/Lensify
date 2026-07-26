import os
import re


def detect_design_patterns(folder_path: str):
    patterns = []

    folders = set()
    files = []
    python_files = []

    # Scan project
    for root, dirs, filenames in os.walk(folder_path):

        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for d in dirs:
            folders.add(d.lower())

        for file in filenames:

            path = os.path.join(root, file)
            files.append(file.lower())

            if file.endswith(".py"):
                python_files.append(path)

    # =====================================================
    # Repository Pattern
    # =====================================================

    if (
        "repository" in folders
        or "repositories" in folders
    ):

        patterns.append({
            "name": "Repository Pattern",
            "confidence": 98,
            "reason": "Repository folder detected."
        })

    # =====================================================
    # MVC Pattern
    # =====================================================

    if (
        "controllers" in folders
        and "models" in folders
    ):

        patterns.append({
            "name": "MVC Pattern",
            "confidence": 95,
            "reason": "Controllers and Models folders found."
        })

    # =====================================================
    # Layered Pattern
    # =====================================================

    if (
        ("services" in folders or "service" in folders)
        and ("repositories" in folders or "repository" in folders)
    ):

        patterns.append({
            "name": "Layered Pattern",
            "confidence": 96,
            "reason": "Service and Repository layers detected."
        })

    # =====================================================
    # Factory Pattern
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if (
                re.search(r"class\s+\w+Factory", code)
                or re.search(r"def\s+create_\w+", code)
            ):

                patterns.append({
                    "name": "Factory Pattern",
                    "confidence": 90,
                    "reason": f"Factory found in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    # =====================================================
    # Singleton Pattern
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if (
                "__new__" in code
                and "_instance" in code
            ):

                patterns.append({
                    "name": "Singleton Pattern",
                    "confidence": 88,
                    "reason": f"Singleton implementation found in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    # =====================================================
    # Builder Pattern
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if re.search(r"class\s+\w+Builder", code):

                patterns.append({
                    "name": "Builder Pattern",
                    "confidence": 90,
                    "reason": f"Builder class found in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    # =====================================================
    # Strategy Pattern
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if (
                "execute(" in code
                and "strategy" in code.lower()
            ):

                patterns.append({
                    "name": "Strategy Pattern",
                    "confidence": 85,
                    "reason": f"Strategy implementation detected in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    # =====================================================
    # Adapter Pattern
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if re.search(r"class\s+\w+Adapter", code):

                patterns.append({
                    "name": "Adapter Pattern",
                    "confidence": 88,
                    "reason": f"Adapter class found in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    # =====================================================
    # Dependency Injection
    # =====================================================

    for file in python_files:

        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()

            if re.search(
                r"def __init__\(self,\s*.*service|repository",
                code,
                re.IGNORECASE,
            ):

                patterns.append({
                    "name": "Dependency Injection",
                    "confidence": 92,
                    "reason": f"Constructor injection detected in {os.path.basename(file)}."
                })

                break

        except Exception:
            continue

    if not patterns:

        patterns.append({
            "name": "No Significant Pattern Detected",
            "confidence": 0,
            "reason": "No common design patterns were identified."
        })

    return {
        "patterns": patterns,
        "total_patterns": len(patterns)
    }
