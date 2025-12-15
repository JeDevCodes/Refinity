from intelligence.tools.base import CodeTool # type: ignore
import subprocess
import tempfile
import os

class PyTestTool(CodeTool):
    def name(self):
        return "pytest"

    def run(self, code):
        with tempfile.TemporaryDirectory() as tmpdirname:
            test_file = os.path.join(tmpdirname, "test_code.py")
            with open(test_file, "w") as f:
                f.write(code)
            result = subprocess.run(["pytest", test_file, "--maxfail=5", "--disable-warnings", "-q"],
                                    capture_output=True, text=True)
        return result
