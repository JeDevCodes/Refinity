import ast
from intelligence.tools.base import CodeTool # type: ignore

class ASTTool(CodeTool):
    def name(self):
        return "ast"

    def run(self, code: str) -> dict:
        """
        Parses code into an abstract syntax tree and extracts function/method/class information.
        """
        tree = ast.parse(code)
        functions = []
        classes = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "lineno": node.lineno,
                    "args": [arg.arg for arg in node.args.args]
                })
            elif isinstance(node, ast.ClassDef):
                classes.append({
                    "name": node.name,
                    "lineno": node.lineno,
                    "methods": [
                        f.name for f in node.body if isinstance(f, ast.FunctionDef)
                    ]
                })

        return {"functions": functions, "classes": classes}
