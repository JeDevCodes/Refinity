from langchain_core.tools import tool

from intelligence.tools.universal.codematrics_tool import CodeMetricsTool

@tool
def run_comment_density_check(code: str) -> dict:
    """
    Checks comment density across any programming language.
    """
    return CodeMetricsTool().run(code)
