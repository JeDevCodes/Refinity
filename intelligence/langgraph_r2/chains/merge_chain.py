from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from intelligence.llms.jelem import jelem_llm



# === Prompt for Review & Refactor ===
merge_prompt = PromptTemplate(
    input_variables=["code1", "code2", "context", "tools_output","language"],
    template="""
You are a code refactorer AI. Given the following 1 user unoptimized code, 2 answered optimized code blocks, context, and analysis from static tools, your task is to review both the optimized codes based on the context(if available) and user code and generate a single code out of these two code in the given :

context: {context}
and the language of code is:{language}

un-fixed user code:
{code}

-----
Code 1 :
{llm_1_output}
-----
Code 2 :
{llm_2_output}

tool insights are :{tools_output}

Now return an improved version of the code from both the given codes, with enhancements and fixes applied. Respond with only the refactored code inside a Python code block nothing else.
"""
)

merge_chain: Runnable = merge_prompt | jelem_llm