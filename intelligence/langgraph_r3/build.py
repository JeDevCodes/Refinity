from langgraph.graph import StateGraph, END
from .state import R3State
from .nodes import llm_1_node, llm_2_node, merge_node

def build_r3_graph():
    builder = StateGraph(R3State)

    # Nodes
    builder.add_node("llm_1", llm_1_node)
    builder.add_node("llm_2", llm_2_node)
    builder.add_node("merge", merge_node)

    # Edges
    builder.set_entry_point("llm1")
    builder.add_edge("llm1", "llm_2")
    builder.add_edge("llm_2", "merge")
    builder.add_edge("merge",END)

    return builder.compile()
