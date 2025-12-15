import subprocess
import tempfile
import os
from intelligence.tools.base import CodeTool

class UnittestTool(CodeTool):
    def name(self):
        return "unittest"

    def run(self, code: str) -> str:
        """
        Writes the code to a temporary file and runs Python's unittest framework on it.
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            test_file = os.path.join(tmpdirname, "test_code.py")
            with open(test_file, "w") as f:
                f.write(code)

            result = subprocess.run(
                ["python", "-m", "unittest", test_file],
                capture_output=True,
                text=True
            )

        return result.stdout
