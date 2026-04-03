from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv();


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)
prompt = PromptTemplate(
    template= "Introduce the {topic} in 4-5 lines",
    input_variables=["topic"]
)


topic = input("Enter the topic you want to know about: ")

formated_prompt = prompt.invoke({'topic': topic})

blog_title = model.invoke(formated_prompt)

print(blog_title)