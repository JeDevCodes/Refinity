from .state import R3State
import json
from intelligence.tools.python.timeit_tool import TimeitTool
from intelligence.langgraph_r3.chains.jelem_chain import jelem_chain
from intelligence.langgraph_r3.chains.llm2_chain import llm2_chain 
from intelligence.langgraph_r3.chains.merge_chain import merge_chain


#jelem
def llm_1_node(state: R3State) -> R3State:

    prompt_input={
        'query':state.get('query','')
    }
    response = jelem_chain.invoke(prompt_input)
    return {**state, "llm_1_output": response}

#llm2
def llm_2_node(state: R3State) -> R3State:
    prompt_input={
        'query':state.get('query','')
    }
    response = llm2_chain.invoke(prompt_input)
    return {**state, "llm_2_output": response}

# Merge LLM Outputs
def merge_node(state: R3State) -> R3State:
    out1 = state.get("llm_1_output", "")
    out2 = state.get("llm_2_output", "")

    prompt_input={
        'llm_1_output': state.get('llm_1_output',''),
        'llm_2_output': state.get('llm_2_output',''),
        'query': state.get('query','')
    }
    
    response = merge_chain.invoke(prompt_input)
    return {**state, "final_output": response}
    