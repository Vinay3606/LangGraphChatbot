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

### 1️⃣ Basic Chatbot

This interface demonstrates a simple conversational AI chatbot built with **LangGraph** and **Ollama**. The chatbot maintains conversation context using **MemorySaver**, allowing it to remember previous messages during the session.

**Highlights**

- 💬 Interactive chat interface
- 🧠 Stateful conversation memory
- ⚡ Fast responses using Qwen2.5:3B
- 🎨 Clean Streamlit UI

<p align="center">
  <img src="assets/100.png" alt="Basic Chatbot" width="900"/>
</p>

---

### 2️⃣ Thread-Based Chatbot with Streaming

This version extends the chatbot with **thread-based conversation management** and **real-time streaming responses**.

Each conversation is assigned a unique thread, allowing users to continue previous chats or start completely new ones. Instead of waiting for the entire response, the chatbot streams tokens one by one, creating a smoother and more interactive chat experience.

**Features**

- 🧵 Multiple chat threads
- ♻️ Resume previous conversations
- ➕ Start a new chat anytime
- 🧠 Persistent memory for every thread
- ⚡ Token-by-token streaming responses
- 💬 Chat history management
- 🎨 Modern Streamlit interface

<p align="center">
  <img src="assets/103.png" alt="Thread-based Chatbot" width="900"/>
</p>

---

## 👨‍💻 Author

**Vinay Choudhary**

If you found this project useful, consider giving it a ⭐ on GitHub.
