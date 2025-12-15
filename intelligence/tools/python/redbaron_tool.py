from redbaron import RedBaron # type: ignore
from intelligence.tools.base import CodeTool # type: ignore

class RedBaronTool(CodeTool):
    def name(self):
        return "redbaron"

    def run(self, code: str) -> dict:
        """
        Parses code using RedBaron for structural insight and transformation capability.
        Returns structure information and docstrings.
        """
        red = RedBaron(code)
        structure = []

        for node in red.find_all("DefNode"):
            structure.append({
                "type": "function",
                "name": node.name,
                "docstring": node.value.dumps() if node.value else "None"
            })

        for node in red.find_all("ClassNode"):
            structure.append({
                "type": "class",
                "name": node.name,
                "docstring": node.value.dumps() if node.value else "None",
                "content": node.dumps()
            })

        return {"structure": structure}
