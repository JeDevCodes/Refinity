import timeit
from intelligence.tools.base import CodeTool

class TimeitTool(CodeTool):
    def name(self):
        return "timeit"

    def run(self, code: str) -> dict:
        """
        Times the execution of a provided code snippet using timeit.
        Only suitable for small snippets or isolated functions.
        """
        try:
            execution_time = timeit.timeit(code, number=5)
            return {"execution_time": execution_time, "runs": 5}
        except Exception as e:
            return {"error": str(e)}
