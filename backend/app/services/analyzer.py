import os
import json

from app.services.dependency_scanner import scan_dependencies
from app.services.performance_analyzer import analyze_performance

def analyze_project(folder_path: str):

    files = []
    total_lines = 0
    project_name = os.path.basename(folder_path)

    # ---------------------------------
    # Default Values
    # ---------------------------------

    languages = set()

    frontend = "Unknown"
    backend = "Unknown"
    database = "Unknown"
    authentication = "Unknown"

    orm = "Unknown"
    testing = "Unknown"
    cloud = "Unknown"

    deployment = "Unknown"

    package_manager = "Unknown"
    dependency_file = None

    project_type = "Unknown"

    has_readme = False

    # ---------------------------------
    # Walk Through Project
    # ---------------------------------

    for root, dirs, filenames in os.walk(folder_path):

        print(f"\nFolder: {root}")

        # Ignore Git folders

        dirs[:] = [
            d for d in dirs
            if not d.startswith(".git")
        ]

        for file in filenames:

            # Ignore hidden/system files

            if file.startswith("."):
                continue

            print("  ", file)

            files.append(file)

            lower = file.lower()

            path = os.path.join(root, file)

            # ---------------------------------
            # Language Detection
            # ---------------------------------

            if lower.endswith(".py"):
                languages.add("Python")

            elif lower.endswith((".js", ".jsx")):
                languages.add("JavaScript")

            elif lower.endswith((".ts", ".tsx")):
                languages.add("TypeScript")

            elif lower.endswith(".java"):
                languages.add("Java")

            elif lower.endswith(".cpp"):
                languages.add("C++")

            elif lower.endswith(".c"):
                languages.add("C")

            elif lower.endswith(".cs"):
                languages.add("C#")

            elif lower.endswith(".go"):
                languages.add("Go")

            elif lower.endswith(".php"):
                languages.add("PHP")

            # ---------------------------------
            # README Detection
            # ---------------------------------

            if lower in (
                "readme.md",
                "readme.txt",
                "readme",
            ):
                has_readme = True

            # ---------------------------------
            # package.json Detection
            # ---------------------------------

            if lower == "package.json":

                package_manager = "npm"
                dependency_file = file

                try:

                    with open(path, "r", encoding="utf-8") as f:
                        package = json.load(f)

                    if package.get("name"):
                        project_name = package["name"]

                    deps = {}
                    deps.update(package.get("dependencies", {}))
                    deps.update(package.get("devDependencies", {}))

                    # Frontend

                    if "react" in deps:
                        frontend = "React"

                    elif "next" in deps:
                        frontend = "Next.js"

                    elif "vue" in deps:
                        frontend = "Vue.js"

                    elif "@angular/core" in deps:
                        frontend = "Angular"

                    # Backend

                    if "express" in deps:
                        backend = "Express.js"

                    elif "@nestjs/core" in deps:
                        backend = "NestJS"

                    # Database

                    if "mongoose" in deps:
                        database = "MongoDB"

                    elif "mysql2" in deps:
                        database = "MySQL"

                    elif "pg" in deps:
                        database = "PostgreSQL"

                    elif "sqlite3" in deps:
                        database = "SQLite"

                    elif "firebase" in deps:
                        database = "Firebase"

                    # Authentication

                    if "jsonwebtoken" in deps:
                        authentication = "JWT"

                    elif "passport" in deps:
                        authentication = "Passport.js"

                    elif "@auth0/auth0-react" in deps:
                        authentication = "Auth0"

                    # Deployment

                    if "vercel" in deps:
                        deployment = "Vercel"

                except Exception:
                    pass

            # ---------------------------------
            # requirements.txt Detection
            # ---------------------------------

            elif lower == "requirements.txt":

                package_manager = "pip"
                dependency_file = file

                try:

                    with open(path, "r", encoding="utf-8") as f:
                        requirements = f.read().lower()

                    if "fastapi" in requirements:
                        backend = "FastAPI"

                    elif "flask" in requirements:
                        backend = "Flask"

                    elif "django" in requirements:
                        backend = "Django"

                    if "sqlalchemy" in requirements:
                        orm = "SQLAlchemy"

                    if (
                        "mysqlclient" in requirements
                        or "pymysql" in requirements
                    ):
                        database = "MySQL"

                    elif "psycopg2" in requirements:
                        database = "PostgreSQL"

                    elif "pymongo" in requirements:
                        database = "MongoDB"

                    if "pyjwt" in requirements:
                        authentication = "JWT"

                    if "pytest" in requirements:
                        testing = "Pytest"

                except Exception:
                    pass

            # ---------------------------------
            # Deployment Detection
            # ---------------------------------

            if lower == "dockerfile":
                deployment = "Docker"

            elif lower in (
                "docker-compose.yml",
                "docker-compose.yaml",
            ):
                deployment = "Docker Compose"

            elif lower == "vercel.json":
                deployment = "Vercel"

            elif lower == "netlify.toml":
                deployment = "Netlify"

            elif lower == "render.yaml":
                deployment = "Render"

            elif lower == "railway.json":
                deployment = "Railway"

            # ---------------------------------
            # Backend File Detection
            # ---------------------------------

            if lower == "manage.py":
                backend = "Django"

            elif lower == "app.py":
                backend = "Flask"

            elif lower == "main.py":

                try:

                    with open(path, "r", encoding="utf-8") as f:

                        code = f.read().lower()

                        if "fastapi(" in code:
                            backend = "FastAPI"

                except Exception:
                    pass

           
            # ---------------------------------
            # Scan File Contents
            # ---------------------------------

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore",
                ) as f:

                    content = f.read()

                total_lines += len(content.splitlines())

                code = content.lower()

                # -----------------------------
                # Frontend Detection
                # -----------------------------

                if frontend == "Unknown":

                    if (
                        "import react" in code
                        or "from 'react'" in code
                        or 'from "react"' in code
                        or "reactdom" in code
                    ):
                        frontend = "React"

                    elif (
                        "next.config" in code
                        or "from 'next'" in code
                        or 'from "next"' in code
                    ):
                        frontend = "Next.js"

                    elif (
                        "createapp(" in code
                        or "vue.createapp" in code
                    ):
                        frontend = "Vue.js"

                    elif (
                        "@angular/core" in code
                        or "angular.module" in code
                    ):
                        frontend = "Angular"

                    elif lower.endswith(
                        (
                            ".html",
                            ".css",
                            ".js",
                        )
                    ):
                        frontend = "HTML/CSS/JavaScript"

                # -----------------------------
                # Backend Detection
                # -----------------------------

                if backend == "Unknown":

                    if (
                        "from flask import" in code
                        or "flask(" in code
                    ):
                        backend = "Flask"

                    elif (
                        "from fastapi import" in code
                        or "fastapi(" in code
                    ):
                        backend = "FastAPI"

                    elif "from django" in code:
                        backend = "Django"

                    elif (
                        "require('express')" in code
                        or 'require("express")' in code
                        or "express()" in code
                    ):
                        backend = "Express.js"

                    elif "@nestjs/core" in code:
                        backend = "NestJS"

                # -----------------------------
                # Database Detection
                # -----------------------------

                if database == "Unknown":

                    if (
                        "mysql.connector" in code
                        or "pymysql" in code
                        or "mysqlclient" in code
                    ):
                        database = "MySQL"

                    elif (
                        "psycopg2" in code
                        or "postgresql" in code
                    ):
                        database = "PostgreSQL"

                    elif (
                        "pymongo" in code
                        or "mongodb" in code
                        or "mongoose" in code
                    ):
                        database = "MongoDB"

                    elif "sqlite3" in code:
                        database = "SQLite"

                    elif "firebase" in code:
                        database = "Firebase"

                # -----------------------------
                # Authentication Detection
                # -----------------------------

                if authentication == "Unknown":

                    if (
                        "pyjwt" in code
                        or "import jwt" in code
                        or "from jwt" in code
                    ):
                        authentication = "JWT"

                    elif "passport" in code:
                        authentication = "Passport.js"

                    elif "oauth" in code:
                        authentication = "OAuth"

                    elif "firebase.auth" in code:
                        authentication = "Firebase Auth"

                # -----------------------------
                # ORM Detection
                # -----------------------------

                if orm == "Unknown":

                    if "sqlalchemy" in code:
                        orm = "SQLAlchemy"

                    elif "mongoose" in code:
                        orm = "Mongoose"

                    elif "prisma" in code:
                        orm = "Prisma"

                    elif "typeorm" in code:
                        orm = "TypeORM"

                # -----------------------------
                # Testing Detection
                # -----------------------------

                if testing == "Unknown":

                    if "pytest" in code:
                        testing = "Pytest"

                    elif "jest" in code:
                        testing = "Jest"

                    elif "vitest" in code:
                        testing = "Vitest"

                    elif "unittest" in code:
                        testing = "unittest"

                # -----------------------------
                # Cloud Detection
                # -----------------------------

                if cloud == "Unknown":

                    if (
                        "import boto3" in code
                        or "from boto3" in code
                    ):
                        cloud = "AWS"

                    elif (
                        "from google.cloud" in code
                        or "import google.cloud" in code
                    ):
                        cloud = "Google Cloud"

                    elif (
                        "from azure" in code
                        or "import azure" in code
                        or "azure.storage" in code
                        or "azure.identity" in code
                    ):
                        cloud = "Azure"

                # -----------------------------
                # AI Framework Detection
                # -----------------------------

                ai_tools = []

                if "openai" in code:
                    ai_tools.append("OpenAI")

                if (
                    "google.genai" in code
                    or "google.generativeai" in code
                ):
                    ai_tools.append("Gemini")

                if "langchain" in code:
                    ai_tools.append("LangChain")

                if "llamaindex" in code:
                    ai_tools.append("LlamaIndex")

                if "tensorflow" in code:
                    ai_tools.append("TensorFlow")

                if (
                    "torch" in code
                    or "pytorch" in code
                ):
                    ai_tools.append("PyTorch")

                if (
                    "sklearn" in code
                    or "scikit-learn" in code
                ):
                    ai_tools.append("Scikit-learn")

                if ai_tools and "AI" not in backend:
                    backend += " + AI"

            except Exception:
                pass
    # ---------------------------------
    # Dependency Scanner
    # ---------------------------------

    deps = scan_dependencies(folder_path)

    if deps:

        if deps.get("backend"):
            backend = deps["backend"]

        if deps.get("database"):
            database = deps["database"]

        if deps.get("authentication"):
            authentication = deps["authentication"]

        if deps.get("orm"):
            orm = deps["orm"]

        if deps.get("testing"):
            testing = deps["testing"]

        if deps.get("cloud"):
            cloud = deps["cloud"]

        if deps.get("frontend"):
            frontend = deps["frontend"]

        if deps.get("deployment"):
            deployment = deps["deployment"]

        if deps.get("package_manager"):
            package_manager = deps["package_manager"]

        if deps.get("dependency_file"):
            dependency_file = deps["dependency_file"]

    # ---------------------------------
    # Final Cleanup
    # ---------------------------------

    if frontend == "":
        frontend = "Unknown"

    if backend == "":
        backend = "Unknown"

    if database == "":
        database = "Unknown"

    if authentication == "":
        authentication = "Unknown"

    if orm == "":
        orm = "Unknown"

    if testing == "":
        testing = "Unknown"

    if cloud == "":
        cloud = "Unknown"

    if deployment == "":
        deployment = "Unknown"

    if package_manager == "":
        package_manager = "Unknown"
       # ---------------------------------
    # Language Output
    # ---------------------------------

    if languages:
        language = " + ".join(sorted(languages))
    else:
        language = "Unknown"

    # ---------------------------------
    # Project Type Detection
    # ---------------------------------

    if frontend != "Unknown" and backend != "Unknown":
        project_type = "Full Stack Web Application"

    elif frontend != "Unknown":
        project_type = "Frontend Application"

    elif backend != "Unknown":
        project_type = "Backend Application"

    elif language == "Python":
        project_type = "Python Application"

    elif language == "Java":
        project_type = "Java Application"

    elif language == "C":
        project_type = "C Application"

    elif language == "C++":
        project_type = "C++ Application"

    else:
        project_type = "Software Project"

    # ---------------------------------
    # Technology Score
    # ---------------------------------

    technology_score = 0

    for value in [
        frontend,
        backend,
        database,
        authentication,
        orm,
        testing,
        cloud,
        deployment,
    ]:
        if value != "Unknown":
            technology_score += 1

    # ---------------------------------
    # Analysis Score
    # ---------------------------------

    analysis_score = 0

    if language != "Unknown":
        analysis_score += 1

    if frontend != "Unknown":
        analysis_score += 1

    if backend != "Unknown":
        analysis_score += 1

    if database != "Unknown":
        analysis_score += 1

    if authentication != "Unknown":
        analysis_score += 1

    if orm != "Unknown":
        analysis_score += 1

    if testing != "Unknown":
        analysis_score += 1

    if cloud != "Unknown":
        analysis_score += 1

    if deployment != "Unknown":
        analysis_score += 1

    if has_readme:
        analysis_score += 1

    # ---------------------------------
    # Return Result
    # ---------------------------------

    return {
    "project_name": project_name,
    "project_type": project_type,
    "language": language,

    "frontend": frontend,
    "backend": backend,
    "database": database,
    "authentication": authentication,

    "orm": orm,
    "testing": testing,
    "cloud": cloud,

    "deployment": deployment,

    "package_manager": package_manager,
    "dependency_file": dependency_file,

    # Boolean
    "readme": has_readme,

    # Required by frontend
    "total_files": len(files),
"total_lines": total_lines,
"files": files,

# Statistics
"total_dependencies": sum(
    value != "Unknown"
    for value in [
        frontend,
        backend,
        database,
        authentication,
        orm,
        testing,
        cloud,
        deployment,
    ]
),

"total_technologies": technology_score,

"technology_score": technology_score,
"analysis_score": analysis_score,
}   