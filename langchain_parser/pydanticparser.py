from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

class Person(BaseModel):
    name: str = Field(..., description="Name of the person")
    age: int = Field(..., gt=18, description="Age of the Person")
    city: str = Field(..., description="Name of the city person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of the fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={
        'format_instruction': parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({
    "place": "Indian"
})

print(result)