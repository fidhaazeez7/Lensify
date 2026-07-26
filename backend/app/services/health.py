def calculate_health(analysis, bugs, security):

    score = 0

    # Documentation
    if analysis["readme"]:
        score += 10

    # Dependency File
    if analysis["dependency_file"]:
        score += 10

    # Technology Detection
    if analysis["frontend"] != "Unknown":
        score += 15

    if analysis["backend"] != "Unknown":
        score += 15

    if analysis["database"] != "Unknown":
        score += 10

    if analysis["authentication"] != "Unknown":
        score += 10

    if analysis["deployment"] != "Unknown":
        score += 10

    # Bugs
    if len(bugs) == 0:
        score += 10

    # Security
    if len(security) == 0:
        score += 10

    score = min(score, 100)

    if score >= 90:
        status = "Excellent"

    elif score >= 75:
        status = "Good"

    elif score >= 60:
        status = "Average"

    else:
        status = "Needs Improvement"

    return {
        "score": score,
        "status": status
    }