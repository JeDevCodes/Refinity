from typing import TypedDict, Optional, List

class R2State(TypedDict, total=False):
    code: str                           # Input code from user
    context: Optional[str]              # Optional context from user
    language: str                       # Detected or selected language
    tools_output: Optional[dict]        # Tool feedback in string format
    llm_1_output: Optional[str]         # Output from JeLem LLM
    llm_2_output: Optional[str]         # Output from DeepSeek LLM
    final_output: Optional[str]         # Merged/refined output to return
    runtime: Optional[str]