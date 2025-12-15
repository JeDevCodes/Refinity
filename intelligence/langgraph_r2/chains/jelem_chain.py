from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from intelligence.llms.jelem import jelem_llm

# === Prompt for Review & Refactor ===
r2_prompt = PromptTemplate(
    input_variables=["code", "context", "tools_output","language"],
    template="""
You are a code reviewer and refactorer AI. Given the following code, context, and analysis from static tools, your task is to review and refactor the code for performance, readability, security, and maintainability.

Context (optional):
{context}

the possible language of the code(might be different):{language}

Original Code:
{code}
tool insights are:{tools_output}"
Now return an improved version of the code, with enhancements and fixes applied. Respond with only the refactored code inside a Python code block.
"""
)

jelem_chain: Runnable = r2_prompt | jelem_llm