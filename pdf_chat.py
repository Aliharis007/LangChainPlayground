import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# Load .env
load_dotenv()

# Setup Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

loader = PyPDFLoader("GANs.pdf") 
pages = loader.load_and_split()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(pages, embeddings)

retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "Summarize this PDF in simple terms"
response = qa_chain.run(query)

print("\n🧠 Chat With PDF Response:\n", response)
