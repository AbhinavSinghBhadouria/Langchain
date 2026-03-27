from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

prompt = PromptTemplate(
    template="Introduce the {topic} in 4-5 lines",
    input_variables=["topic"]
)

parser = StrOutputParser()
chain = prompt | model | parser
# formatted_prompt = prompt.invoke({'topic':'Artificial Intelligence'})

# result = model.invoke(formatted_prompt)

result = chain.invoke({'topic':'Aritificial Intelligence'})
print(result)

chain.get_graph().print_ascii()