import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

print("API KEY =", os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_project_review(
    analysis: dict,
    bugs: list,
    security: list,
    health: dict,
):
    """
    Generates an AI review of the uploaded software project.
    """

    prompt = f"""
You are a senior software architect.

Analyze the following project information and return ONLY valid JSON.

Project Details:
{json.dumps(analysis, indent=2)}

Bug Report:
{json.dumps(bugs, indent=2)}

Security Report:
{json.dumps(security, indent=2)}

Health Report:
{json.dumps(health, indent=2)}

Return this exact JSON structure:

{{
    "rating": "Excellent | Good | Average | Poor",
    "summary": "...",

    "strengths": [
        "...",
        "...",
        "..."
    ],

    "weaknesses": [
        "...",
        "...",
        "..."
    ],

    "recommendations": [
        "...",
        "...",
        "..."
    ]
}}

Do not return markdown.
Do not use ```json.
Return JSON only.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "rating": "Unknown",
            "summary": "Unable to generate AI review.",
            "strengths": [],
            "weaknesses": [],
            "recommendations": [],
            "error": str(e),
        }
    