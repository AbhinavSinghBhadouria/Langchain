from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
import os   
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.llms import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS


load_dotenv()

model= ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)


# load the document
loader = TextLoader("docs.txtm") 
documents = loader.load()

# split the text into smaller chunks 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
docs = text_splitter.split_document(documents)

# convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings(model=model))

# create a retriever ( fetch relevant documents based on query)
retriever = vectorstore.as_retriever()

# manually retrieve relevant documents
query = "What are the key takeaways from the documents?"
retrieved_docs = retriever.get_relevant_documents(query)

# combine Retrieved text into a single prompt
combined_text = "\n".join([doc.page_content for doc in retrieved_docs])

 