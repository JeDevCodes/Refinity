from intelligence.tools.base import CodeTool # type: ignore
from radon.complexity import cc_visit # type: ignore

class RadonTool(CodeTool):
    def name(self):
        return "radon"

    def run(self, code):
        blocks = cc_visit(code)
        return [{"name": b.name, "complexity": b.complexity, "type": b.type, "lineno": b.lineno} for b in blocks]
