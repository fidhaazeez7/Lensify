import ast
import os


class PerformanceVisitor(ast.NodeVisitor):
    def __init__(self):
        self.issues = []
        self.function_lengths = []
        self.current_function = None

    def visit_FunctionDef(self, node):
        self.current_function = node.name

        if hasattr(node, "end_lineno"):
            length = node.end_lineno - node.lineno + 1

            self.function_lengths.append(length)

            if length > 50:
                self.issues.append({
                    "type": "Long Function",
                    "severity": "Medium",
                    "line": node.lineno,
                    "description": f"Function '{node.name}' is {length} lines long.",
                    "recommendation": "Split the function into smaller reusable functions."
                })

        self.generic_visit(node)

    def visit_For(self, node):
        for child in ast.iter_child_nodes(node):

            if isinstance(child, (ast.For, ast.While)):
                self.issues.append({
                    "type": "Nested Loop",
                    "severity": "Medium",
                    "line": node.lineno,
                    "description": "Nested loop detected.",
                    "recommendation": "Reduce nested iterations using dictionaries, sets or better algorithms."
                })

        self.generic_visit(node)

    def visit_While(self, node):
        for child in ast.iter_child_nodes(node):

            if isinstance(child, (ast.For, ast.While)):
                self.issues.append({
                    "type": "Nested Loop",
                    "severity": "Medium",
                    "line": node.lineno,
                    "description": "Nested loop detected.",
                    "recommendation": "Reduce nested iterations."
                })

        self.generic_visit(node)

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            if node.func.id in ["open", "input"]:
                self.issues.append({
                    "type": "Blocking IO",
                    "severity": "Low",
                    "line": node.lineno,
                    "description": f"Blocking call '{node.func.id}()' detected.",
                    "recommendation": "Consider asynchronous alternatives if performance is important."
                })

        self.generic_visit(node)


def analyze_python_file(filepath):

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    try:
        tree = ast.parse(code)
    except Exception:
        return [], 100

    visitor = PerformanceVisitor()
    visitor.visit(tree)

    score = 100

    score -= len(visitor.issues) * 3

    if score < 0:
        score = 0

    return visitor.issues, score

def analyze_performance(project_path):

    all_issues = []
    total_score = 0
    file_count = 0

    summary = {
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for root, _, files in os.walk(project_path):

        for file in files:

            if not file.endswith(".py"):
                continue

            filepath = os.path.join(root, file)

            issues, score = analyze_python_file(filepath)

            # Add filename to each issue
            for issue in issues:
                issue["file"] = os.path.relpath(filepath, project_path)

                severity = issue["severity"]

                if severity in summary:
                    summary[severity] += 1

                all_issues.append(issue)

            # Large file detection
            try:

                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = len(f.readlines())

                if lines > 500:

                    all_issues.append({
                        "type": "Large File",
                        "severity": "Low",
                        "file": os.path.relpath(filepath, project_path),
                        "line": 1,
                        "description": f"File contains {lines} lines.",
                        "recommendation": "Split this file into smaller modules."
                    })

                    summary["Low"] += 1
                    score -= 5

            except Exception:
                pass

            total_score += max(score, 0)
            file_count += 1

    # Remove duplicate issues
    unique = []

    seen = set()

    for issue in all_issues:

        key = (
            issue["type"],
            issue["file"],
            issue["line"]
        )

        if key not in seen:
            seen.add(key)
            unique.append(issue)

    all_issues = unique

    if file_count == 0:
        overall_score = 100
    else:
        overall_score = round(total_score / file_count)

    # Performance Rating
    if overall_score >= 90:
        rating = "Excellent"

    elif overall_score >= 75:
        rating = "Good"

    elif overall_score >= 60:
        rating = "Average"

    else:
        rating = "Poor"

    return {
        "score": overall_score,
        "rating": rating,
        "issues": all_issues,
        "summary": {
            "total": len(all_issues),
            "high": summary["High"],
            "medium": summary["Medium"],
            "low": summary["Low"]
        }
    }