from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import Optional, TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write all key themes discussed in the review"]
    summary: Annotated[str, "A brief of the review"]
    sentiment: Annotated[str, "return sentiment of the review either positive, negative or neutral"]
    pros: Annotated[Optional[list[str]], "write all the pros"]
    cons: Annotated[Optional[list[str]], "write all the cons"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
""")

print(result)
print(result["summary"])
print(result["sentiment"])