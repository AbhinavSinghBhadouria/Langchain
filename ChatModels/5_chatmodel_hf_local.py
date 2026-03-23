from langchain_huggingface import HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",  # Much smaller and faster model
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=50  # Shorter response
    )
)

# Simple chat loop
print("Chat with the model! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    result = llm.invoke(user_input)
    print(f"Model: {result}")