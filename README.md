# 🤖 LangGraph Chatbot

A conversational AI chatbot built using **LangGraph**, **LangChain**, **Ollama**, and **Streamlit**. This project demonstrates how to create a stateful chatbot with conversation memory and thread-based chat sessions using LangGraph.

> **Project Status:** 🚧 Under Development

---

## 📌 Current Features

* ✅ LangGraph StateGraph workflow
* ✅ ChatOllama (Qwen2.5:3B)
* ✅ Persistent conversation memory using MemorySaver
* ✅ Streamlit Chat UI
* ✅ Thread-based conversation support
* ✅ Streaming AI responses
* ✅ Modular backend and frontend architecture

---

## 🛠️ Tech Stack

* Python
* LangGraph
* LangChain
* Ollama
* Qwen2.5:3B
* Streamlit
* Python Dotenv

---

## 📂 Project Structure

```text
LangGraph_chatbot/
│
├── chatbot_backend.py
├── chatbot_frontend.py
├── streamlit_frontend.py
├── streamlit_frontend_threading.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Vinay3606/LangGraph_chatbot.git
```

Move into the project

```bash
cd LangGraph_chatbot
```

Create a virtual environment

```bash
python -m venv bot
```

Activate the environment

### Windows

```bash
bot\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run chatbot_frontend.py
```

or

```bash
streamlit run streamlit_frontend.py
```

---

## 🚀 Current Implementation

* LangGraph StateGraph
* START → Chat Node → END
* Conversation Memory
* Thread-based Chat Sessions
* Streaming Responses
* Streamlit User Interface

---

## 📈 Upcoming Features

* RAG (Retrieval-Augmented Generation)
* FAISS Vector Database
* Document Upload (PDF, DOCX)
* Multiple Chat Sessions
* Chat History Sidebar
* Memory Management
* Tool Calling
* AI Agents
* Web Search Integration
* Image Understanding
* Authentication
* Deployment

---

## 📷 Screenshots

Coming Soon...

---

## 👨‍💻 Author

**Vinay Choudhary**

If you found this project useful, consider giving it a ⭐ on GitHub.
