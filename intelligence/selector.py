# File: refinity/intelligence/tools/selector.py

from intelligence.utils.tool_wrappers_python import *
from intelligence.utils.tool_wrappers_java import *
from intelligence.utils.tool_wrappers_universal import *

def get_tools_by_language(language: str) -> list:
    """
    Returns a list of LangChain-compatible tools based on the programming language.
    """
    language = language.lower()

    universal = [run_comment_density_check]

    if language == "python":
        return [
            run_ast_analysis,
            run_bandit_analysis,
            run_pylint_check,
            run_mypy_check,
            run_redbaron_structure,
            run_timeit_benchmark,
            run_unittest_runner,
            run_pytest_runner,
            run_radon_analysis,
        ] + universal

    elif language == "java":
        return [
            run_javaparser_analysis,
            run_checkstyle_lint,
        ] + universal

    else:
        return universal
