from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def heading(text, styles):
    return Paragraph(f"<b>{text}</b>", styles["Heading2"])


def generate_report(data: dict) -> BytesIO:

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.HexColor("#0F172A")

    subtitle_style = styles["BodyText"]
    subtitle_style.alignment = TA_CENTER
    subtitle_style.textColor = colors.grey

    story = []

    # ======================================================
    # Title
    # ======================================================

    story.append(
        Paragraph(
            "Lensify AI Software Analysis Report",
            title_style,
        )
    )

    story.append(
        Paragraph(
            "Automatically Generated Software Engineering Report",
            subtitle_style,
        )
    )

    story.append(Spacer(1, 0.35 * inch))

    generated = datetime.now().strftime("%d %B %Y  %I:%M %p")

    story.append(
        Paragraph(
            f"<b>Generated:</b> {generated}",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    analysis = data.get("analysis", {})
    health = data.get("health", {})
    bugs = data.get("bugs", [])
    security = data.get("security", [])

    # ======================================================
    # Project Overview
    # ======================================================

    story.append(heading("Project Overview", styles))

    overview = [
        ["Property", "Value"],
        ["Project Name", analysis.get("project_name", "Unknown")],
        ["Project Type", analysis.get("project_type", "Unknown")],
        ["Language", analysis.get("language", "Unknown")],
        ["Frontend", analysis.get("frontend", "Not Detected")],
        ["Backend", analysis.get("backend", "Not Detected")],
        ["Database", analysis.get("database", "Not Detected")],
        [
            "Authentication",
            analysis.get("authentication", "Not Detected"),
        ],
        [
            "Package Manager",
            analysis.get("package_manager", "Unknown"),
        ],
        [
            "README",
            "Available"
            if analysis.get("readme")
            else "Not Found",
        ],
    ]

    overview_table = Table(
        overview,
        colWidths=[180, 280],
    )

    overview_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563EB")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#DBEAFE")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(overview_table)

    story.append(Spacer(1, 0.35 * inch))

    # ===== Part 2 Starts Here =====
        # ======================================================
    # Project Statistics
    # ======================================================

    story.append(heading("Project Statistics", styles))

    statistics = [
        ["Metric", "Value"],
        ["Total Files", str(analysis.get("total_files", 0))],
        ["Lines of Code", str(analysis.get("total_lines", 0))],
        ["Dependencies", str(analysis.get("total_dependencies", 0))],
        ["Technologies", str(analysis.get("total_technologies", 0))],
    ]

    stats_table = Table(
        statistics,
        colWidths=[180, 280],
    )

    stats_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#059669")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#D1FAE5")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(stats_table)

    story.append(Spacer(1, 0.30 * inch))

    # ======================================================
    # Project Health
    # ======================================================

    story.append(heading("Project Health", styles))

    health_table = Table(
        [
            ["Health Metric", "Value"],
            ["Score", f"{health.get('score', 0)}%"],
            ["Status", health.get("status", "Unknown")],
        ],
        colWidths=[180, 280],
    )

    health_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DC2626")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#FEE2E2")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(health_table)

    story.append(Spacer(1, 0.30 * inch))

    # ======================================================
    # Bugs
    # ======================================================

    story.append(heading("Detected Bugs", styles))

    if bugs:

        bug_rows = [["Title", "Severity"]]

        for bug in bugs:
            bug_rows.append(
                [
                    bug.get("title", "Unknown"),
                    bug.get("severity", "Unknown"),
                ]
            )

        bug_table = Table(
            bug_rows,
            colWidths=[350, 110],
        )

        bug_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EA580C")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )

        story.append(bug_table)

    else:

        story.append(
            Paragraph(
                "No bugs were detected during analysis.",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.35 * inch))

    # ===== Part 3 Starts Here =====
        # ======================================================
    # Security Issues
    # ======================================================

    story.append(heading("Security Issues", styles))

    if security:

        security_rows = [["Issue", "Severity"]]

        for issue in security:
            security_rows.append(
                [
                    issue.get("title", "Unknown"),
                    issue.get("severity", "Unknown"),
                ]
            )

        security_table = Table(
            security_rows,
            colWidths=[350, 110],
        )

        security_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7C3AED")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )

        story.append(security_table)

    else:

        story.append(
            Paragraph(
                "No security vulnerabilities were detected.",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.30 * inch))

    # ======================================================
    # AI Review
    # ======================================================

    ai_review = data.get("ai_review", {})

    story.append(heading("AI Review", styles))

    rating = ai_review.get("rating", "Not Available")

    story.append(
        Paragraph(
            f"<b>Overall Rating:</b> {rating}",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.15 * inch))

    strengths = ai_review.get("strengths", [])

    story.append(
        Paragraph("<b>Strengths</b>", styles["Heading3"])
    )

    if strengths:
        for item in strengths:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph("No strengths available.", styles["BodyText"])
        )

    story.append(Spacer(1, 0.15 * inch))

    weaknesses = ai_review.get("weaknesses", [])

    story.append(
        Paragraph("<b>Weaknesses</b>", styles["Heading3"])
    )

    if weaknesses:
        for item in weaknesses:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph("No weaknesses available.", styles["BodyText"])
        )

    story.append(Spacer(1, 0.15 * inch))

    recommendations = ai_review.get("recommendations", [])

    story.append(
        Paragraph("<b>Recommendations</b>", styles["Heading3"])
    )

    if recommendations:
        for item in recommendations:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph(
                "No recommendations available.",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.35 * inch))

    # ======================================================
    # Conclusion
    # ======================================================

    story.append(heading("Conclusion", styles))

    story.append(
        Paragraph(
            "This report was automatically generated by "
            "<b>Lensify AI</b>. The analysis summarizes the project's "
            "overall quality, health, detected bugs, security findings, "
            "and AI-generated recommendations to help improve software "
            "quality and maintainability.",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ===== Part 4 Starts Here =====
        # ======================================================
    # Footer
    # ======================================================

    story.append(
        Spacer(1, 0.30 * inch)
    )

    story.append(
        Paragraph(
            "<font color='#64748B'>"
            "Generated automatically by <b>Lensify AI</b><br/>"
            "Software Engineering Project Analysis Platform"
            "</font>",
            subtitle_style,
        )
    )

    story.append(
        Spacer(1, 0.15 * inch)
    )

    story.append(
    Paragraph(
        "<font color='#94A3B8'>"
        "© Lensify AI • Software Analysis Platform"
        "</font>",
        subtitle_style,
    )
)
    # ======================================================
    # Build PDF
    # ======================================================

    doc.build(story)

    buffer.seek(0)

    return buffer