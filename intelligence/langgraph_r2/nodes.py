from langchain_core.runnables import Runnable
from .state import R2State
import black
import isort
import json
from .selectors import select_tools
from intelligence.tools.python.timeit_tool import TimeitTool
from intelligence.langgraph_r2.chains.jelem_chain import jelem_chain
from intelligence.langgraph_r2.chains.llm2_chain import llm2_chain 
from intelligence.langgraph_r2.chains.merge_chain import merge_chain 


def run_tools_node(state: R2State) -> R2State:
    tools = select_tools(state["language"])
    tool_outputs = {}

    for tool in tools:
        try:
            result = tool.invoke(state["code"])
            tool_outputs[tool.name] = result
        except Exception as e:
            tool_outputs[tool.name] = f"Failed: {str(e)}"

    return {**state, "tools_output": tool_outputs}

#jelem
def llm_1_node(state: R2State) -> R2State:

    prompt_input={
        'code':state['code'],
        'context': state.get('context',''),
        'language':state.get('language',''),
        'tools_output': json.dumps(state.get('tools_output',''), indent=2)
    }
    response = jelem_chain.invoke(prompt_input)
    return {**state, "llm_1_output": response}

#llm2
def llm_2_node(state: R2State) -> R2State:
    prompt_input={
        'code':state['code'],
        'context': state.get('context',''),
        'language':state.get('language',''),
        'tools_output': json.dumps(state.get('tools_output',''), indent=2)
    }
    response = llm2_chain.invoke(prompt_input)
    return {**state, "llm_2_output": response}

# Merge LLM Outputs
def merge_node(state: R2State) -> R2State:
    out1 = state.get("llm_1_output", "")
    out2 = state.get("llm_2_output", "")
    prompt_input={
        'code':state['code'],
        'llm_1_output': state.get('llm_1_output',''),
        'llm_2_output': state.get('llm_2_output',''),
        'context': state.get('context',''),
        'language':state.get('language',''),
        'tools_output': json.dumps(state.get('tools_output',''), indent=2)
    }
    response = merge_chain.invoke(prompt_input)
    return {**state, "final_output": response}

def runtime_node(state: R2State)-> R2State:
    timer=TimeitTool('python')
    response=timer.run(state.get('final_output'),'')
    try:
        code = isort.code(code)
        code = black.format_str(code, mode=black.Mode())
    except Exception as e:
        print(f"[WARN] Formatting failed: {e}")
    return {**state, "runtime": response,'final_output':code}

    