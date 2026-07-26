import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai(
    question: str,
    analysis: dict,
    bugs: list,
    security: list,
    health: dict,
    performance: dict,
    documentation: dict,
    architecture: dict,
    technology: dict,
) -> str:

    prompt = f"""
You are Lensify AI, an expert software engineering assistant.

Your job is to answer ONLY using the analysis results below.

If the answer is not available in the analysis, clearly say that Lensify could not detect that information.

==========================
PROJECT INFORMATION
==========================

{json.dumps(analysis, indent=2)}

==========================
TECHNOLOGY STACK
==========================

{json.dumps(technology, indent=2)}

==========================
ARCHITECTURE
==========================

{json.dumps(architecture, indent=2)}

==========================
HEALTH
==========================

{json.dumps(health, indent=2)}

==========================
PERFORMANCE
==========================

{json.dumps(performance, indent=2)}

==========================
DOCUMENTATION
==========================

{json.dumps(documentation, indent=2)}

==========================
BUG REPORT
==========================

{json.dumps(bugs, indent=2)}

==========================
SECURITY REPORT
==========================

{json.dumps(security, indent=2)}

==========================
USER QUESTION
==========================

{question}

Instructions:

- Answer in clear English.
- Use bullet points where appropriate.
- If the user asks how to improve the project, prioritise High severity issues first.
- Explain security vulnerabilities in simple terms.
- Explain bugs in simple language.
- If asked for a summary, summarise the uploaded project.
- Never invent information that is not present in the analysis.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Unable to contact Gemini: {e}"