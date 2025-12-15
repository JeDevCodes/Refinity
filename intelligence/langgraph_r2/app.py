# from guesslang import Guess
from .build import build_r2_graph
from .state import R2State

graph = build_r2_graph()

def run_r2(code: str, context: str) -> dict:
    input_state: R2State = {
        "code": code,
        "context": context,
        # "language": language  
    }

    result = graph.invoke(input_state)
    return {
        "refactored_code": result.get("final_output"),
        "llm_1_output": result.get("llm_1_output"),
        "llm_2_output": result.get("llm_2_output"),
        "tool_feedback": result.get("tools_output")
    }
