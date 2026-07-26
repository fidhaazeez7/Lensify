import json
from pathlib import Path


def parse_dependencies(project_path: str):
    project = Path(project_path)

    detected = {
        "frontend": set(),
        "backend": set(),
        "database": set(),
        "authentication": set(),
        "deployment": set(),
        "testing": set(),
        "package_manager": set(),
    }

    # ---------------- package.json ----------------

    package_json = project / "package.json"

    if package_json.exists():
        detected["package_manager"].add("npm")

        try:
            data = json.loads(package_json.read_text())

            deps = {}
            deps.update(data.get("dependencies", {}))
            deps.update(data.get("devDependencies", {}))

            for lib in deps:

                name = lib.lower()

                if "react" == name:
                    detected["frontend"].add("React")

                elif "next" == name:
                    detected["frontend"].add("Next.js")

                elif "vue" == name:
                    detected["frontend"].add("Vue")

                elif "angular" in name:
                    detected["frontend"].add("Angular")

                elif "express" == name:
                    detected["backend"].add("Express.js")

                elif "mongoose" == name:
                    detected["database"].add("MongoDB")

                elif "firebase" == name:
                    detected["database"].add("Firebase")

                elif "supabase" in name:
                    detected["database"].add("Supabase")

                elif "jest" == name:
                    detected["testing"].add("Jest")

        except Exception:
            pass

    # ---------------- requirements.txt ----------------

    requirements = project / "requirements.txt"

    if requirements.exists():

        detected["package_manager"].add("pip")

        text = requirements.read_text().lower()

        if "flask" in text:
            detected["backend"].add("Flask")

        if "fastapi" in text:
            detected["backend"].add("FastAPI")

        if "django" in text:
            detected["backend"].add("Django")

        if "sqlalchemy" in text:
            detected["database"].add("SQLAlchemy")

        if "pymysql" in text:
            detected["database"].add("MySQL")

        if "psycopg2" in text:
            detected["database"].add("PostgreSQL")

        if "pytest" in text:
            detected["testing"].add("Pytest")

    return {
        key: list(value)
        for key, value in detected.items()
    }