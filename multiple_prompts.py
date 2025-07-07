import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Load Groq API key
load_dotenv()

# Setup Groq model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Send messages (System + Human)
response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is blockchain?"),
    HumanMessage(content="And what can I build using it?")
])

print("\nGroq LLaMa Chat-style Response:\n", response.content)
