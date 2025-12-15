from .build import build_r3_graph
from .state import R3State

graph = build_r3_graph()

def run_r3(query: str) -> dict:
    input_state: R3State = {
        "query": query
    }

    result = graph.invoke(input_state)
    return {
        "generated_code": result.get("final_output"),
        # "llm_1_output": result.get("llm_1_output"),
        # "llm_2_output": result.get("llm_2_output")
    }
