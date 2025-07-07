import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API Key from .env
load_dotenv()

# Define the LLM using Groq + LLaMA3
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Create a prompt template
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain the topic '{topic}' to a 10-year-old in simple language."
)

chain = LLMChain(llm=llm, prompt=template)
response = chain.run("Blockchain")

print("\nPromptTemplate Response:\n", response)
