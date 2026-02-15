import ast

def parse_code(code: str):
    return ast.parse(code)

def show_ast(tree):
    return ast.dump(tree, indent=2)

def format_code(tree):
    return ast.unparse(tree)

if __name__ == "__main__":
    code = """
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
"""

    tree = parse_code(code)

    print("====== AST OUTPUT ======")
    print(show_ast(tree))

    print("\n====== FORMATTED CODE ======")
    print(format_code(tree))

