from intelligence.tools.base import CodeTool # type: ignore
import subprocess
import tempfile
import os
import json

class BanditTool(CodeTool):
    def name(self):
        return "bandit"

    def run(self, code):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode())
            tmp.flush()
            result = subprocess.run(["bandit", "-f", "json", tmp.name], capture_output=True, text=True)
            os.unlink(tmp.name)
        return json.loads(result.stdout)
