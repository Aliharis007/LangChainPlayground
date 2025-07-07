# ✨LangChainPlayground

This repository contains a collection of hands-on experiments and projects using **LangChain**, an open-source framework for developing applications powered by language models. The goal of this project is to explore various capabilities of LLMs such as prompt engineering, memory management, PDF document querying, and agent-based interactions.

---

## 📂 Folder Structure

```

LangChainPlayground/
│
├── .gitignore             # Ignored files such as .env
├── .env                   # Environment variables (API keys, etc.)
├── README.md              # You're reading it :)
├── GANs.pdf               # PDF file used for testing document querying
├── agent.py               # LangChain agent setup and tool integration
├── chat_memory.py         # Memory usage demonstration in LLM chats
├── llm_call.py            # Basic LLM prompt-response structure
├── multiple_prompts.py    # Using multiple prompt templates in LangChain
├── pdf_chat.py            # Chat with PDF via LangChain and embedding
├── prompttemp.py          # PromptTemplate customization and chaining

```

---

## 🧠 What is LangChain?

**LangChain** is a framework built to make it easier to develop LLM-powered applications using components like:

- **PromptTemplates**
- **Memory (ConversationBuffer, Summary, etc.)**
- **Chains and Agents**
- **Document Loaders and VectorStores**

It helps in connecting language models to external data sources, APIs, tools, and more.

Official website: [https://www.langchain.com](https://www.langchain.com)

---

## 📝 Project Description

This project serves as a mini playground to explore LangChain’s functionality through various modules and scenarios:

### 🔹 `llm_call.py`
- A simple demonstration of sending a prompt to an LLM (like OpenAI or HuggingFace) and receiving a response.
- Shows how to initialize the LLM and configure temperature, model name, etc.

### 🔹 `prompttemp.py`
- Demonstrates how to use `PromptTemplate` to build reusable and dynamic prompts.
- Templates can be filled in real-time with user input or external data.

### 🔹 `chat_memory.py`
- Implements conversation memory using `ConversationBufferMemory`.
- Shows how LLM can retain context over multiple turns of conversation.

### 🔹 `pdf_chat.py`
- Uses `PyPDFLoader` and `Chroma` VectorStore to allow users to chat with a document (`GANs.pdf` in this case).
- Embeds text using a model (like OpenAI embeddings or HuggingFace).
- Useful for building document Q&A systems.

### 🔹 `multiple_prompts.py`
- Demonstrates switching between multiple `PromptTemplates` dynamically.
- Useful for multi-step reasoning or context switching in conversations.

### 🔹 `agent.py`
- Uses LangChain **Agents** to interact with tools (like calculator, search, etc.).
- Shows how to give an agent access to multiple tools and let it decide what to use based on the input.

---

## 🔐 Environment Variables

All sensitive keys (e.g., OpenAI API keys) should be stored in the `.env` file. Example format:

```

OPENAI\_API\_KEY=your\_openai\_api\_key\_here

````

Make sure `.env` is included in `.gitignore` to prevent it from being pushed to GitHub.

---

## 📄 Dependencies

You can install the necessary dependencies using:

```bash
pip install -r requirements.txt
````

(If you don’t have one yet, generate a `requirements.txt` with:
`pip freeze > requirements.txt`)

Commonly used packages include:

* `langchain`
* `openai`
* `chromadb`
* `python-dotenv`
* `PyPDF2`
* `tiktoken`
* `faiss-cpu` or `chromadb` (for vector storage)

---

## 📘 PDF Chat Example (`GANs.pdf`)

The `pdf_chat.py` module shows how to:

* Load and split the `GANs.pdf` using LangChain’s document loaders.
* Embed document chunks.
* Enable semantic search and interaction with the PDF through queries.

You can change `GANs.pdf` to any other PDF you want to chat with.

---

## ⚙️ How to Run

Set up the `.env` file with your API key(s). Then simply run the desired script using:

```bash
python llm_call.py
```

Or:

```bash
python pdf_chat.py
```

> Make sure your environment supports the required API keys and internet access if needed.

---

## 🚀 Future Ideas / TODOs

* Add Streamlit UI for interactive demo.
* Connect agents to external APIs like weather, calculator, or web scraping.
* Integrate LangChain Expression Language (LCEL).
* Use HuggingFace models offline for privacy.

---

## 🤝 Contributing

Feel free to open issues or pull requests if you'd like to add more use cases or improve existing ones. Let’s make this LangChain playground even more awesome!

---

## 🙌 Acknowledgements

* [LangChain Official Docs](https://docs.langchain.com)
* [OpenAI API](https://platform.openai.com/)
* [Python dotenv](https://pypi.org/project/python-dotenv/)

```
