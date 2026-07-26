import json
import os


def _read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().lower()
    except:
        return ""


def scan_dependencies(folder_path: str):
    print("=" * 60)
    print("Scanning Project:", folder_path)

    result = {
        "backend": None,
        "database": None,
        "authentication": None,
        "orm": None,
        "testing": None,
        "cloud": None,
        "frontend": None,
        "deployment": None,
        "package_manager": None,
        "dependency_file": None,
    }

    for root, _, files in os.walk(folder_path):

        # -------------------------------------------------
        # requirements.txt
        # -------------------------------------------------

        if "requirements.txt" in files:

            path = os.path.join(root, "requirements.txt")
            text = _read_file(path)

            result["package_manager"] = "pip"
            result["dependency_file"] = "requirements.txt"

            # Backend

            if "fastapi" in text:
                result["backend"] = "FastAPI"

            elif "flask" in text:
                result["backend"] = "Flask"

            elif "django" in text:
                result["backend"] = "Django"

            # Database

            if "psycopg2" in text:
                result["database"] = "PostgreSQL"

            elif "mysqlclient" in text or "pymysql" in text:
                result["database"] = "MySQL"

            elif "pymongo" in text:
                result["database"] = "MongoDB"

            elif "sqlite3" in text:
                result["database"] = "SQLite"

            elif "redis" in text:
                result["database"] = "Redis"

            # ORM

            if "sqlalchemy" in text:
                result["orm"] = "SQLAlchemy"

            elif "django-orm" in text:
                result["orm"] = "Django ORM"

            # Authentication

            if (
                "python-jose" in text
                or "pyjwt" in text
                or "jwt" in text
            ):
                result["authentication"] = "JWT"

            elif "oauthlib" in text:
                result["authentication"] = "OAuth"

            # Testing

            if "pytest" in text:
                result["testing"] = "Pytest"

            elif "unittest" in text:
                result["testing"] = "unittest"

            # Cloud

            if "boto3" in text:
                result["cloud"] = "AWS"

            elif "google-cloud" in text:
                result["cloud"] = "Google Cloud"

            elif "azure-storage" in text:
                result["cloud"] = "Azure"

        # -------------------------------------------------
        # package.json
        # -------------------------------------------------

        if "package.json" in files:

            path = os.path.join(root, "package.json")

            try:

                with open(path, "r", encoding="utf-8") as f:
                    package = json.load(f)

                deps = {}

                deps.update(package.get("dependencies", {}))
                deps.update(package.get("devDependencies", {}))

                result["package_manager"] = "npm"
                result["dependency_file"] = "package.json"

                # Frontend

                if "react" in deps:
                    result["frontend"] = "React"

                elif "next" in deps:
                    result["frontend"] = "Next.js"

                elif "vue" in deps:
                    result["frontend"] = "Vue.js"

                elif "@angular/core" in deps:
                    result["frontend"] = "Angular"

                elif "svelte" in deps:
                    result["frontend"] = "Svelte"

                # Backend

                if "express" in deps:
                    result["backend"] = "Express.js"

                elif "@nestjs/core" in deps:
                    result["backend"] = "NestJS"

                # Database

                if "mongoose" in deps:
                    result["database"] = "MongoDB"

                elif "pg" in deps:
                    result["database"] = "PostgreSQL"

                elif "mysql2" in deps:
                    result["database"] = "MySQL"

                elif "sqlite3" in deps:
                    result["database"] = "SQLite"

                elif "firebase" in deps:
                    result["database"] = "Firebase"

                elif "redis" in deps:
                    result["database"] = "Redis"

                # Authentication

                if "jsonwebtoken" in deps:
                    result["authentication"] = "JWT"

                elif "passport" in deps:
                    result["authentication"] = "Passport.js"

                elif "firebase-admin" in deps:
                    result["authentication"] = "Firebase Auth"

                # Testing

                if "jest" in deps:
                    result["testing"] = "Jest"

                elif "mocha" in deps:
                    result["testing"] = "Mocha"

            except Exception as e:
                print(e)

        # -------------------------------------------------
        # Docker
        # -------------------------------------------------

        if "dockerfile" in [f.lower() for f in files]:
            result["deployment"] = "Docker"

        if "docker-compose.yml" in files or "docker-compose.yaml" in files:
            result["deployment"] = "Docker Compose"

        # -------------------------------------------------
        # Java
        # -------------------------------------------------

        if "pom.xml" in files:
            result["package_manager"] = "Maven"
            result["dependency_file"] = "pom.xml"

        if "build.gradle" in files:
            result["package_manager"] = "Gradle"
            result["dependency_file"] = "build.gradle"

        # -------------------------------------------------
        # PHP
        # -------------------------------------------------

        if "composer.json" in files:
            result["package_manager"] = "Composer"
            result["dependency_file"] = "composer.json"

        # -------------------------------------------------
        # Deployment
        # -------------------------------------------------

        if "vercel.json" in files:
            result["deployment"] = "Vercel"

        if "netlify.toml" in files:
            result["deployment"] = "Netlify"

        if "render.yaml" in files:
            result["deployment"] = "Render"

    print("\nDetected Technologies\n")

    for key, value in result.items():
        print(f"{key:20}: {value}")

    print("=" * 60)

    return result