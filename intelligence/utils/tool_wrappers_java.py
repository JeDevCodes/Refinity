from langchain_core.tools import tool

from intelligence.tools.java.ast_tool import JavaASTTool
from intelligence.tools.java.pmd_tool import PMDTool

@tool
def run_javaparser_analysis(code: str) -> dict:
    """
    Parses Java code structure using JavaParser (external integration).
    """
    return JavaASTTool('java').run(code)

@tool
def run_checkstyle_lint(code: str) -> dict:
    """
    Checks Java code style using Checkstyle.
    """
    return PMDTool('java').run(code)
