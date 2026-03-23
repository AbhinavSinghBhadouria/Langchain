from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

Chat_Template = ChatPromptTemplate({
    ('system','you are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, What is {topic}')
})


prompt= Chat_Template.invoke({'domain': 'cricket', 'topic':'Dusra'})

print(prompt)