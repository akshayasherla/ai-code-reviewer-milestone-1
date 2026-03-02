import ast

class ErrorDetector(ast.NodeVisitor):
    def __init__(self):
        self.violations = []
        self.defined_vars = set()
        self.used_vars = set()
        self.score = 100

    def visit_FunctionDef(self, node):
        if not node.name.islower() or "_" not in node.name:
            self.violations.append(
                f"Function '{node.name}' should be snake_case at line {node.lineno}"
            )
            self.score -= 10
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if not node.name[0].isupper():
            self.violations.append(
                f"Class '{node.name}' should be PascalCase at line {node.lineno}"
            )
            self.score -= 10
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined_vars.add(node.id)
            if len(node.id) == 1:
                self.violations.append(
                    f"Variable '{node.id}' name too short at line {node.lineno}"
                )
                self.score -= 5
        elif isinstance(node.ctx, ast.Load):
            self.used_vars.add(node.id)
        self.generic_visit(node)

def analyze_code(code_string):
    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        return {"success": False, "error": f"Syntax Error: {e}"}

    detector = ErrorDetector()
    detector.visit(tree)

    unused = detector.defined_vars - detector.used_vars
    for var in unused:
        detector.violations.append(f"Unused variable '{var}'")
        detector.score -= 5

    return {"success": True, "violations": detector.violations, "score": max(detector.score, 0)}

if __name__ == "__main__":
    sample_code = """
class badclass:
    def BadFunctionName(self):
        a = 10
        return a
"""
    print(analyze_code(sample_code))