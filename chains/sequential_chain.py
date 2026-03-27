from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variales=['topic'],
)

prompt2 = PromptTemplate(
    template='Generate 5 pointer summary for the {text}',
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser

result =chain.invoke({"topic":"One Sided love"})

print(result)

chain.get_graph().print_ascii()