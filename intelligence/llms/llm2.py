import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
API_KEY=os.getenv("LLM2_API_KEY")

llm2 = ChatOpenAI(
    base_url="https://api.deepseek.com",  # Example endpoint
    api_key=API_KEY,
    model="deepseek-coder-70b-instruct",  # Or whichever variant you're using
    temperature=0.7,
    max_tokens=4096
)
