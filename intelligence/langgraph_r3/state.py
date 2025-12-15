from typing import TypedDict, Optional, List

class R3State(TypedDict, total=False):
    query: str
    llm_1_output: Optional[str]
    llm_2_output: Optional[str]
    final_output: Optional[str]