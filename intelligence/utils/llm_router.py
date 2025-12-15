from typing import Literal
from intelligence.llms.jelem import jelem_llm
from langchain_community.llms import DeepSeek

# Define available LLMs
AVAILABLE_MODELS = {
    "jelem": jelem_llm,
    "deepseek": DeepSeek(model_name="deepseek-coder:6.7b", temperature=0.4)
}

def get_llm_by_name(name: Literal["jelem", "deepseek"]):
    """
    Manually select an LLM by name.
    """
    if name not in AVAILABLE_MODELS:
        raise ValueError(f"[LLM Router] Unknown LLM name: {name}")
    return AVAILABLE_MODELS[name]

def auto_route(prompt: str):
    """
    Automatically select the best LLM based on prompt analysis.
    Currently defaults to JeLem for all.
    Extend this logic in future based on use-case.
    """
    # Example heuristic (extend later)
    if "optimize" in prompt.lower() or "refactor" in prompt.lower():
        return AVAILABLE_MODELS["jelem"]
    elif "build" in prompt.lower() or "generate" in prompt.lower():
        return AVAILABLE_MODELS["deepseek"]
    else:
        return AVAILABLE_MODELS["jelem"]
