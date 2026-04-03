from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
import os

load_dotenv()

prompt1 = PromptTemplate(
    template=' Generate a weet about {topic}',
    input_variables=['topic']
)


prompt2= PromptTemplate(
    template='Generate a linkedIn post about {topic}',
    input_variables=['topic']
)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

parser = StrOutputParser()


chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin_post': RunnableSequence(prompt2, model, parser)
})


result = chain.invoke({'topic': 'Artificial Intelligence'})

print(result)


