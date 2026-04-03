from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI


load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",       
    api_key=os.getenv("GEMINI_API_KEY"),
)

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("Hi there how are you"))

prompt = PromptTemplate(
    template="Wrtie a joke about {topic}",
    input_variables=['topic']
)


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count': RunnableLambda(word_counter)
    }
)

final_chain= RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic' : 'AI'}))

