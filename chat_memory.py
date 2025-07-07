import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

#Setup memory
memory = ConversationBufferMemory()

#create conversation chain
conversation=ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(conversation.run("Hi, I am Ali, and my brother's name is Saad"))
print(conversation.run("What's my brother's name?"))
print(conversation.run("Now explain langchain"))