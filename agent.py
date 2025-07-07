import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Useful for answering questions about current events or the web"
    )
]
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Run Agent
response = agent.run("What is the latest AI news in 2025?")
print(response)
