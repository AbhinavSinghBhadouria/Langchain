from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents=[
    "Delhi is the capital of india",
    "india is a peaceful country",
    "but somepeoples alwayhs try to make it turbulant/restless"
]
embedding= OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_documents(documents)

print(result)
