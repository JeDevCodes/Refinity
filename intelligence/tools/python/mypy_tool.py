from intelligence.tools.base import CodeTool # type: ignore
import subprocess
import tempfile
import os

class MyPyTool(CodeTool):
    def name(self):
        return "mypy"

    def run(self, code):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode())
            tmp.flush()
            result = subprocess.run(["mypy", tmp.name], capture_output=True, text=True)
            os.unlink(tmp.name)
        return result.stdout
