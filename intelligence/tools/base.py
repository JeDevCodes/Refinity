from abc import ABC, abstractmethod

class CodeTool(ABC):
    def __init__(self, language: str = "generic"):
        self.language = language

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def run(self, code: str) -> dict:
        """
        Process the code and return a structured output (JSON/dict).
        """
        pass
