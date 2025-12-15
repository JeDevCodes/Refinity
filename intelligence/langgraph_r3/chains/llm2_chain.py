from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from intelligence.llms.llm2 import llm2

r3_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are a pro code generator, your task is to generate the code for performance, readability, security, and maintainability based on user query.
-----
query:
{query}
-----
Now return the code, with enhancements and fixes applied. Respond with only the block, just the code, nothing else.
"""
)

llm2_chain: Runnable = r3_prompt | llm2