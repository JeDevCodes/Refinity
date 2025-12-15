from langgraph.graph import StateGraph, END
from .state import R2State
from .nodes import run_tools_node, llm_1_node, llm_2_node, merge_node, runtime_node

def is_python(state):
    if state.get('language','')=="python":
        return 'yes'
    else:
        return 'no'

def build_r2_graph():
    builder = StateGraph(R2State)

    # Nodes
    builder.add_node("run_tools", run_tools_node)
    builder.add_node("llm_1", llm_1_node)
    builder.add_node("llm_2", llm_2_node)
    builder.add_node("merge", merge_node)
    builder.add_node("runtime", runtime_node)

    # Edges
    builder.set_entry_point("run_tools")
    builder.add_edge("run_tools", "llm_1")
    builder.add_edge("run_tools", "llm_2")  
    builder.add_edge("llm_1", "merge")
    builder.add_edge("llm_2", "merge")
    builder.add_conditional_edges(
        "merge",
        is_python,
        {
            "yes":"runtime_node",
            "no":END
        }
    )
    builder.add_edge("runtime_node", END)

    return builder.compile()
