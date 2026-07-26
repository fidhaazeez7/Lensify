from pathlib import Path


def classify_project(project_path: str):

    project = Path(project_path)

    if (project / "package.json").exists():
        return "JavaScript Web Application"

    if (project / "requirements.txt").exists():
        return "Python Application"

    if (project / "pom.xml").exists():
        return "Java Application"

    if (project / "composer.json").exists():
        return "PHP Application"

    return "Software Project"