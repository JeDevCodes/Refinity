from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from intelligence.llms.jelem import jelem_llm



# === Prompt for Review & Refactor ===
merge_prompt = PromptTemplate(
    input_variables=["llm_1_output", "llm_2_output", "query"],
    template="""
You are given with 2 answer codes for a given user query try to choose one code from it and then if required perform updation for better, optimized, secure code output:
-----
user query: {query}
-----
answer code 1 :
{llm_1_output}
-----
answer code 2 :
{llm_2_output}


Now return an improved version of the code from both the given codes, with enhancements and fixes applied only if required. Respond with only choosen output code only nothing else.
"""
)

jelem_chain: Runnable = merge_prompt | jelem_llm