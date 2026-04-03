from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os


load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)


template = PromptTemplate(
    template="Write a jokoe about {topic}",
    input_variables =['topic']
)



parser = StrOutputParser()

chain = RunnableSequence(template , model , parser)

print(chain.invoke({'topic':'AI'}))