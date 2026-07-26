import os


def detect_frameworks(folder_path: str):
    detected = {
        "frontend": None,
        "backend": None,
        "database": None,
        "communication": None,
        "deployment": None,
    }

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read().lower()
            except Exception:
                continue

            # ---------- Backend ----------

            if "from fastapi import" in content or "fastapi(" in content:
                detected["backend"] = "FastAPI"

            elif "from flask import" in content:
                detected["backend"] = "Flask"

            elif "express()" in content or "require('express')" in content:
                detected["backend"] = "Express.js"

            elif "@restcontroller" in content:
                detected["backend"] = "Spring Boot"

            # ---------- Frontend ----------

            if "import react" in content or "from 'react'" in content:
                detected["frontend"] = "React"

            elif "@angular/core" in content:
                detected["frontend"] = "Angular"

            elif "createapp(" in content and "vue" in content:
                detected["frontend"] = "Vue"

            elif "next.config" in file.lower():
                detected["frontend"] = "Next.js"

            # ---------- Database ----------

            if "sqlalchemy" in content:
                detected["database"] = "SQLAlchemy"

            elif "mongoose.connect" in content:
                detected["database"] = "MongoDB"

            elif "psycopg2" in content:
                detected["database"] = "PostgreSQL"

            elif "sqlite3" in content:
                detected["database"] = "SQLite"

            elif "supabase" in content:
                detected["database"] = "Supabase"

            elif "firebase" in content:
                detected["database"] = "Firebase"

            # ---------- Communication ----------

            if "@app.get" in content or "@router.get" in content:
                detected["communication"] = "REST API"

            elif "graphql" in content:
                detected["communication"] = "GraphQL"

            elif "websocket" in content or "socket.io" in content:
                detected["communication"] = "WebSocket"

            # ---------- Deployment ----------

            if "dockerfile" == file.lower():
                detected["deployment"] = "Docker"

            elif "docker-compose.yml" == file.lower():
                detected["deployment"] = "Docker Compose"

            elif "vercel.json" == file.lower():
                detected["deployment"] = "Vercel"

            elif "render.yaml" == file.lower():
                detected["deployment"] = "Render"

            elif "railway.json" == file.lower():
                detected["deployment"] = "Railway"

    return detected