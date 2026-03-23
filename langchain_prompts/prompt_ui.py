from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
import os
load_dotenv()

model = ChatGoogleGenerativeAI(
model="gemini-2.5-flash", 
   google_api_key=os.getenv("GEMINI_API_KEY")
)

st.header("Research Tool")

# user_input= st.text_input('Enter your prompt') // it is a kind of static prompt

paper_name=st.selectbox("Select Research paper name",["Select...","Attention is all you need","BERT: Pre-training of Bidirectional Transformer","GPT-3: Language Models are few-shot learners","Diffusion Models Beat GAN's on image Synthesis"])

style_input=st.selectbox("Select Explanation Style",["Beginner-friendly","Technical","Code-oriented","Mathematical"])

length_input=st.selectbox("Select Explanation length",["Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(Detailed explanation)"])

template=load_prompt("template.json")
# template = PromptTemplate(
#     input_variables=["paper_name", "style_input", "length_input"],
#     template="""
# Please summarize the research paper titled "{paper_name}" with the following specifications:

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
# - Include relevant mathematical equations if present in the paper.
# - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
# - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """
# )

# prompt= template.invoke({
#     'paper_name':paper_name,
#     'style_input':style_input,
#     'length_input':length_input
# })
# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)

    # we can do the above two things in one go

if st.button('Summarize'):
        chain= template | model
        result=chain.invoke({
             'paper_name':paper_name,
             'style_input':style_input,
             'length_input':length_input
        })
        st.write(result.content)