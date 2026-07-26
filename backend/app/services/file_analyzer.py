from pathlib import Path

from app.services.technology_database import TECHNOLOGIES


def scan_project(project_path: str):
    """
    Scan all files in the project and detect technologies
    using the central technology database.
    """

    detected = {}

    # Initialize result
    for category in TECHNOLOGIES:
        detected[category] = []

    # Scan every file
    for file in Path(project_path).rglob("*"):

        if not file.is_file():
            continue

        try:
            text = file.read_text(errors="ignore").lower()
        except Exception:
            continue

        # Check every technology in every category
        for category, technologies in TECHNOLOGIES.items():

            for technology, patterns in technologies.items():

                for pattern in patterns:

                    if pattern.lower() in text:

                        if technology not in detected[category]:
                            detected[category].append(technology)

                        break

    return detected