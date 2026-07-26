import os
import re


def add_issue(issues, title, severity, file, line, description, fix):
    issues.append({
        "title": title,
        "severity": severity,
        "file": file,
        "line": line,
        "description": description,
        "fix": fix,
    })

PATTERNS = [
    {
        "title": "Hardcoded API Key",
        "severity": "High",
        "regex": r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
        "description": "API key is hardcoded in source code.",
        "fix": "Store secrets in environment variables."
    },
    {
        "title": "Hardcoded Password",
        "severity": "High",
        "regex": r'password\s*=\s*["\'][^"\']+["\']',
        "description": "Password is hardcoded.",
        "recommendation": "Use environment variables or a secret manager."
    },
    {
        "title": "AWS Access Key",
        "severity": "High",
        "regex": r'AKIA[0-9A-Z]{16}',
        "description": "Possible AWS Access Key detected.",
        "recommendation": "Rotate the key immediately."
    },
    {
        "title": "JWT Secret",
        "severity": "High",
        "regex": r'jwt[_-]?secret\s*=\s*["\'][^"\']+["\']',
        "description": "JWT secret is hardcoded.",
        "recommendation": "Move the secret to an environment variable."
    },
]


def scan_security(folder_path: str):

    issues = []

    for root, _, files in os.walk(folder_path):

        for file in files:

            if not file.endswith((".py", ".js", ".ts")):
                continue

            path = os.path.join(root, file)

            try:

                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                code = "".join(lines)

                # ----------------------------
                # Regex-based checks
                # ----------------------------

                for pattern in PATTERNS:

                    for i, line in enumerate(lines, start=1):

                        if re.search(pattern["regex"], line, re.IGNORECASE):

                            add_issue(
                                issues,
                                pattern["title"],
                                pattern["severity"],
                                file,
                                i,
                                pattern["description"],
                                pattern["recommendation"],
                            )

                # ----------------------------
                # eval()
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "eval(" in line:

                        add_issue(
                            issues,
                            "Use of eval()",
                            "High",
                            file,
                            i,
                            "eval() executes arbitrary code.",
                            "Avoid eval(). Use safer alternatives.",
                        )

                # ----------------------------
                # exec()
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "exec(" in line:

                        add_issue(
                            issues,
                            "Use of exec()",
                            "High",
                            file,
                            i,
                            "exec() executes arbitrary Python code.",
                            "Avoid exec().",
                        )

                # ----------------------------
                # SQL Injection
                # ----------------------------

                sql_patterns = [
                    "execute(",
                    "cursor.execute(",
                ]

                for i, line in enumerate(lines, start=1):

                    if any(x in line for x in sql_patterns):

                        if "%" in line or "+" in line or "format(" in line or "f\"" in line:

                            add_issue(
                                issues,
                                "Possible SQL Injection",
                                "High",
                                file,
                                i,
                                "SQL query appears to be built dynamically.",
                                "Use parameterized queries.",
                            )

                # ----------------------------
                # subprocess shell=True
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "shell=True" in line:

                        add_issue(
                            issues,
                            "shell=True Usage",
                            "Medium",
                            file,
                            i,
                            "shell=True can introduce command injection risks.",
                            "Avoid shell=True when possible.",
                        )

                # ----------------------------
                # Weak Hash
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "md5(" in line.lower():

                        add_issue(
                            issues,
                            "Weak Hash Algorithm",
                            "Medium",
                            file,
                            i,
                            "MD5 is cryptographically broken.",
                            "Use SHA-256 or bcrypt.",
                        )

                    if "sha1(" in line.lower():

                        add_issue(
                            issues,
                            "Weak Hash Algorithm",
                            "Medium",
                            file,
                            i,
                            "SHA1 is considered insecure.",
                            "Use SHA-256.",
                        )

                # ----------------------------
                # Debug Mode
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "debug=true" in line.lower():

                        add_issue(
                            issues,
                            "Debug Mode Enabled",
                            "Low",
                            file,
                            i,
                            "Debug mode should not be enabled in production.",
                            "Disable debug mode.",
                        )

                # ----------------------------
                # HTTP URLs
                # ----------------------------

                for i, line in enumerate(lines, start=1):

                    if "http://" in line.lower():

                        add_issue(
                            issues,
                            "Insecure HTTP URL",
                            "Low",
                            file,
                            i,
                            "HTTP traffic is unencrypted.",
                            "Use HTTPS.",
                        )

            except Exception:
                pass

    return issues