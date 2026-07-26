import ast
import os


def add_bug(bugs, title, severity, file, line, description, fix):
    bugs.append({
        "title": title,
        "severity": severity,
        "file": file,
        "line": line,
        "description": description,
        "fix": fix,
    })


class BugVisitor(ast.NodeVisitor):
    def __init__(self, filename, bugs):
        self.filename = filename
        self.bugs = bugs

    # -----------------------------
    # Function Analysis
    # -----------------------------
    def visit_FunctionDef(self, node):

        # Missing docstring
        if ast.get_docstring(node) is None:
            add_bug(
                self.bugs,
                "Missing Function Docstring",
                "Low",
                self.filename,
                node.lineno,
                f'Function "{node.name}" has no docstring.',
                "Add a descriptive docstring."
            )

        # Long function
        if hasattr(node, "end_lineno") and node.end_lineno:
            length = node.end_lineno - node.lineno

            if length > 50:
                add_bug(
                    self.bugs,
                    "Long Function",
                    "Medium",
                    self.filename,
                    node.lineno,
                    f'Function "{node.name}" is {length} lines long.',
                    "Split it into smaller helper functions."
                )

        # Too many parameters
        if len(node.args.args) > 5:
            add_bug(
                self.bugs,
                "Too Many Parameters",
                "Medium",
                self.filename,
                node.lineno,
                f'Function "{node.name}" has {len(node.args.args)} parameters.',
                "Reduce parameters or group them into an object."
            )

        # Mutable default arguments
        for default in node.args.defaults:

            if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                add_bug(
                    self.bugs,
                    "Mutable Default Argument",
                    "High",
                    self.filename,
                    node.lineno,
                    "Mutable default arguments can cause unexpected behaviour.",
                    "Use None as the default value and initialize inside the function."
                )

        # Empty function
        if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            add_bug(
                self.bugs,
                "Empty Function",
                "Low",
                self.filename,
                node.lineno,
                f'Function "{node.name}" is empty.',
                "Implement the function or remove it."
            )

        self.generic_visit(node)

    # -----------------------------
    # Exception Handling
    # -----------------------------
    def visit_ExceptHandler(self, node):

        if node.type is None:
            add_bug(
                self.bugs,
                "Broad Exception Handling",
                "Medium",
                self.filename,
                node.lineno,
                "Using 'except:' catches every exception.",
                "Catch only specific exception types."
            )

        elif isinstance(node.type, ast.Name):

            if node.type.id == "Exception":
                add_bug(
                    self.bugs,
                    "Broad Exception Handling",
                    "Medium",
                    self.filename,
                    node.lineno,
                    "Using 'except Exception' catches every exception.",
                    "Catch specific exceptions."
                )

        if len(node.body) == 1:

            stmt = node.body[0]

            if isinstance(stmt, ast.Pass):
                add_bug(
                    self.bugs,
                    "Empty Except Block",
                    "Medium",
                    self.filename,
                    node.lineno,
                    "Exception is ignored.",
                    "Handle or log the exception."
                )

        self.generic_visit(node)

    # -----------------------------
    # Imports
    # -----------------------------
    def visit_ImportFrom(self, node):

        for alias in node.names:

            if alias.name == "*":
                add_bug(
                    self.bugs,
                    "Wildcard Import",
                    "Low",
                    self.filename,
                    node.lineno,
                    "Wildcard imports reduce readability.",
                    "Import only required names."
                )

        self.generic_visit(node)

    # -----------------------------
    # Function Calls
    # -----------------------------
    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            # eval()
            if node.func.id == "eval":
                add_bug(
                    self.bugs,
                    "Use of eval()",
                    "High",
                    self.filename,
                    node.lineno,
                    "Using eval() can execute arbitrary Python code.",
                    "Use ast.literal_eval() or another safer parser."
                )

            # exec()
            if node.func.id == "exec":
                add_bug(
                    self.bugs,
                    "Use of exec()",
                    "High",
                    self.filename,
                    node.lineno,
                    "Using exec() can execute arbitrary Python code.",
                    "Avoid exec() whenever possible."
                )

        self.generic_visit(node)

    # -----------------------------
    # Loops
    # -----------------------------
    def visit_While(self, node):

        if isinstance(node.test, ast.Constant):

            if node.test.value is True:
                add_bug(
                    self.bugs,
                    "Potential Infinite Loop",
                    "High",
                    self.filename,
                    node.lineno,
                    "Infinite while True loop detected.",
                    "Ensure the loop has a proper exit condition."
                )

        self.generic_visit(node)


def scan_bugs(folder_path: str):

    bugs = []

    for root, _, files in os.walk(folder_path):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            try:

                with open(path, "r", encoding="utf-8") as f:
                    source = f.read()

                # TODO / FIXME comments
                for i, line in enumerate(source.splitlines(), start=1):

                    upper = line.upper()

                    if "TODO" in upper:
                        add_bug(
                            bugs,
                            "TODO Comment",
                            "Low",
                            file,
                            i,
                            "TODO comment found.",
                            "Complete or remove the TODO."
                        )

                    if "FIXME" in upper:
                        add_bug(
                            bugs,
                            "FIXME Comment",
                            "Medium",
                            file,
                            i,
                            "FIXME comment found.",
                            "Resolve the issue before production."
                        )

                tree = ast.parse(source)

                visitor = BugVisitor(file, bugs)
                visitor.visit(tree)

            except SyntaxError:

                add_bug(
                    bugs,
                    "Syntax Error",
                    "High",
                    file,
                    1,
                    "Python syntax error detected.",
                    "Fix the syntax error."
                )

            except Exception:
                pass

    return bugs