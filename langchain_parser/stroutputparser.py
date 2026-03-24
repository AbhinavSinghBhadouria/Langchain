from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
   
)

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary of the following text:\n{text}',
    input_variables=['text']
)

# ✅ use format() instead of invoke()
prompt1 = template1.format(topic='black hole')
result = model.invoke(prompt1)

prompt2 = template2.format(text=result.content)
result1 = model.invoke(prompt2)

print(result1.content)
