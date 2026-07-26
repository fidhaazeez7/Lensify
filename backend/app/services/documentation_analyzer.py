import ast
import os


def analyze_documentation(project_path: str):
    readme = False
    docstrings = 0
    comments = 0
    api_docs = False

    suggestions = []

    python_files = 0

    for root, _, files in os.walk(project_path):
        for file in files:
            path = os.path.join(root, file)
            lower = file.lower()

            # README detection
            if lower in ("readme.md", "readme.txt", "readme"):
                readme = True

            # Analyse Python files
            if lower.endswith(".py"):
                python_files += 1

                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        source = f.read()

                    # Count comments
                    for line in source.splitlines():
                        if line.strip().startswith("#"):
                            comments += 1

                    # FastAPI docs
                    if (
                        "FastAPI(" in source
                        or "docs_url" in source
                        or "openapi" in source
                    ):
                        api_docs = True

                    tree = ast.parse(source)

                    # Module docstring
                    if ast.get_docstring(tree):
                        docstrings += 1

                    # Function/Class docstrings
                    for node in ast.walk(tree):
                        if isinstance(
                            node,
                            (
                                ast.FunctionDef,
                                ast.AsyncFunctionDef,
                                ast.ClassDef,
                            ),
                        ):
                            if ast.get_docstring(node):
                                docstrings += 1

                except Exception:
                    pass

    score = 100

    if not readme:
        score -= 20
        suggestions.append("Add a README.md file.")

    if docstrings < 5:
        score -= 20
        suggestions.append("Add more function and class docstrings.")

    if comments < 10:
        score -= 10
        suggestions.append("Increase code comments where necessary.")

    if not api_docs:
        score -= 10
        suggestions.append("Enable API documentation (Swagger/OpenAPI).")

    score = max(score, 0)

    if score >= 90:
        status = "Excellent"
    elif score >= 75:
        status = "Good"
    elif score >= 60:
        status = "Average"
    else:
        status = "Poor"

    coverage = f"{score}%"

    return {
        "score": score,
        "status": status,
        "readme": readme,
        "docstrings": docstrings,
        "comments": comments,
        "api_docs": api_docs,
        "coverage": coverage,
        "suggestions": suggestions,
    }