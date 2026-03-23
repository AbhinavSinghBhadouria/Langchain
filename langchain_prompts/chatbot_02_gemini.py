from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3,
    max_tokens=100
)

history = [SystemMessage(content="You are a helpful AI assistant. Answer clearly and concisely.")]

while True:
    user_input = input("user: ")

    if user_input == "exit":
        break

    history.append(HumanMessage(content=user_input))
    
    result = model.invoke(history)
    
    history.append(AIMessage(content=result.content))
    
    print("AI:", result.content)

print(history)