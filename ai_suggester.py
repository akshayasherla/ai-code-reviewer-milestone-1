import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def get_ai_suggestions(code_string):
    prompt = f"""
You are an experienced coding teacher.
Review the following Python code and provide:
1. Errors (if any)
2. Style issues (PEP8)
3. Optimization suggestions
4. Time & space complexity (if applicable)

Code:
{code_string}
"""
    result = model.invoke(prompt)
    print(result.content)

if __name__ == "__main__":
    code = """
def addNumbers(a,b):
    return a+b
"""
    get_ai_suggestions(code)