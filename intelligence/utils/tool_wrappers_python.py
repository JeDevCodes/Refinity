from langchain_core.tools import tool

from intelligence.tools.python.ast_tool import ASTTool
from intelligence.tools.python.bandit_tools import BanditTool
from intelligence.tools.python.pylint_tool import PylintTool
from intelligence.tools.python.mypy_tool import MyPyTool
from intelligence.tools.python.redbaron_tool import RedBaronTool
from intelligence.tools.python.timeit_tool import TimeitTool
from intelligence.tools.python.unittest_tool import UnittestTool
from intelligence.tools.python.pytest_tool import PyTestTool
from intelligence.tools.python.radon import RadonTool

@tool
def run_ast_analysis(code: str) -> dict:
    """
    Analyzes Python code using the AST module to return structural metadata.
    """
    return ASTTool('python').run(code)

@tool
def run_bandit_analysis(code: str) -> dict:
    """
    Scans Python code for security issues using Bandit.
    """
    return BanditTool('python').run(code)

@tool
def run_pylint_check(code: str) -> dict:
    """
    Lints Python code for syntax/style errors using Pylint.
    """
    return PylintTool('python').run(code)

@tool
def run_mypy_check(code: str) -> dict:
    """
    Checks Python code for type errors using MyPy.
    """
    return MyPyTool('python').run(code)

@tool
def run_redbaron_structure(code: str) -> dict:
    """
    Extracts structure and docstrings from code using RedBaron.
    """
    return RedBaronTool('python').run(code)

@tool
def run_timeit_benchmark(code: str) -> dict:
    """
    Benchmarks execution time of given Python functions using Timeit.
    """
    return TimeitTool('python').run(code)

@tool
def run_unittest_runner(code: str) -> dict:
    """
    Runs unittests found in the code using Python's unittest module.
    """
    return UnittestTool('python').run(code)

@tool
def run_pytest_runner(code: str) -> dict:
    """
    Runs tests using pytest and returns the results.
    """
    return PyTestTool('python').run(code)

@tool
def run_radon_analysis(code: str) -> dict:
    """
    Analyzes code complexity using Radon.
    """
    return RadonTool('python').run(code)

