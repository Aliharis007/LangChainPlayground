import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

#loading groq key from .env
load_dotenv()

#setting up Chatgroq using llama3
llm=ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",
)

#Prompt to test
response=llm.invoke([
    HumanMessage(content="Explain langchain in simple language so that even a kid can undrstand it!")
])

print("\nGroq Llama response:\n",response.content)