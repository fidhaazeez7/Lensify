"""
Technology Database
-------------------
Central database for Lensify Technology Detection Engine.
"""

TECHNOLOGIES = {

    # --------------------------
    # Frontend
    # --------------------------
    "frontend": {

        "React": [
            "react",
            "react-dom",
            "jsx",
            "tsx"
        ],

        "Next.js": [
            "next",
            "next.config",
            "next/router"
        ],

        "Vue": [
            "vue"
        ],

        "Angular": [
            "@angular"
        ],

        "Svelte": [
            "svelte"
        ],

        "HTML": [
            "<html",
            "<!doctype html"
        ],

        "CSS": [
            ".css",
            "@media",
            ":root"
        ],

        "JavaScript": [
            ".js",
            "function ",
            "const ",
            "let ",
            "var "
        ],

        "TypeScript": [
            ".ts",
            ".tsx",
            "interface ",
            "type "
        ],

        "Bootstrap": [
            "bootstrap"
        ],

        "Tailwind CSS": [
            "tailwind",
            "@tailwind"
        ]
    },

    # --------------------------
    # Backend
    # --------------------------
    "backend": {

        "Flask": [
            "from flask",
            "import flask"
        ],

        "FastAPI": [
            "from fastapi",
            "FastAPI("
        ],

        "Django": [
            "from django",
            "manage.py"
        ],

        "Express.js": [
            "express("
        ],

        "NestJS": [
            "@nestjs"
        ],

        "Spring Boot": [
            "@SpringBootApplication"
        ],

        "Laravel": [
            "laravel"
        ]
    },

    # --------------------------
    # Database
    # --------------------------
    "database": {

        "MySQL": [
            "mysql",
            "pymysql",
            "mysql.connector"
        ],

        "PostgreSQL": [
            "postgres",
            "psycopg2"
        ],

        "MongoDB": [
            "mongoose",
            "mongodb",
            "pymongo"
        ],

        "SQLite": [
            "sqlite3"
        ],

        "Redis": [
            "redis"
        ],

        "Firebase": [
            "firebase"
        ],

        "Supabase": [
            "supabase"
        ]
    },

    # --------------------------
    # Authentication
    # --------------------------
    "authentication": {

        "JWT": [
            "jwt",
            "jsonwebtoken"
        ],

        "OAuth": [
            "oauth"
        ],

        "Flask-Login": [
            "flask_login"
        ],

        "Passport.js": [
            "passport"
        ]
    },

    # --------------------------
    # Testing
    # --------------------------
    "testing": {

        "Pytest": [
            "pytest"
        ],

        "Jest": [
            "jest"
        ],

        "Cypress": [
            "cypress"
        ]
    },

    # --------------------------
    # Deployment
    # --------------------------
    "deployment": {

        "Docker": [
            "dockerfile",
            "FROM python",
            "FROM node"
        ],

        "Docker Compose": [
            "docker-compose"
        ],

        "Railway": [
            "railway"
        ],

        "Render": [
            "render.yaml"
        ],

        "Vercel": [
            "vercel"
        ],

        "Netlify": [
            "netlify"
        ]
    },

    # --------------------------
    # Package Managers
    # --------------------------
    "package_manager": {

        "npm": [
            "package.json"
        ],

        "pip": [
            "requirements.txt"
        ],

        "Maven": [
            "pom.xml"
        ],

        "Gradle": [
            "build.gradle"
        ],

        "Composer": [
            "composer.json"
        ]
    }
}