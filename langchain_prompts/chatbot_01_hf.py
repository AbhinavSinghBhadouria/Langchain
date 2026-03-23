from langchain_huggingface import HuggingFacePipeline
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint // phele hmm iska use krr rhe the to hmne llm use kiya. tha
# Use gpt2-medium for better quality responses (better than distilgpt2)
model = HuggingFacePipeline.from_model_id(
    model_id="gpt2-medium",
    task="text-generation",
)

print("Chatbot ready! Type 'exit' to quit.")
print("Note: Better responses require better models. This uses GPT2-Medium.")
chathistory=[]
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
    # Prepare prompt and invoke model
    prompt = "\n".join(chathistory + [user_input])
    result = model.invoke(prompt)

    # HuggingFacePipeline may return a plain string, not an object
    if hasattr(result, 'content'):
        reply = result.content
    else:
        reply = str(result)

    chathistory.append(user_input)
    chathistory.append(reply)

    print("AI:", reply)

print(chathistory)