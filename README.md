# 🤖 Multi-Agent RAG Assistant

> A modular multi-agent system for Retrieval-Augmented Generation (RAG) demonstrating collaborative AI reasoning.

---

## 🧠 Overview

This project implements a **multi-agent Retrieval-Augmented Generation (RAG) system** with a modular and extensible architecture.

Instead of relying on a single model, the system separates responsibilities into independent agents:

- **Retriever Agent** → retrieves relevant documents from a knowledge base  
- **Reasoner Agent** → generates structured answers based on retrieved context  

This design reflects modern trends in **agent-based AI systems**, enabling better scalability, interpretability, and modularity.

---

## 🎯 Motivation

Modern AI systems increasingly rely on:
- Retrieval-augmented pipelines  
- Modular reasoning components  
- Multi-agent collaboration  

This project demonstrates how these ideas can be implemented in a simple but practical system.

---

## ✨ Features

- 🔎 Vector similarity search using FAISS  
- 🧩 Embedding generation via SentenceTransformers  
- 🤖 Modular agent-based architecture  
- 📚 Context-aware answer generation  
- ⚡ Lightweight and extensible design  

---

## 🏗️ Architecture

User Query  
↓  
Retriever Agent  
↓  
Relevant Documents  
↓  
Reasoner Agent  
↓  
Final Answer  

---

## 📂 Project Structure

multi-agent-rag/  
│  
├── src/  
│   ├── retriever.py  
│   ├── reasoner.py  
│   └── utils.py  
│  
├── data/  
│   └── docs.txt  
│  
├── main.py  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation

pip install -r requirements.txt

---

## ▶️ Usage

python main.py

---

## 🧪 Example

You: What causes floods?  

Agent:  
Based on the retrieved information, floods often occur due to heavy rainfall and poor drainage systems.

---

## 🚀 Future Improvements

- Integrate real LLMs (OpenAI / local models)  
- Add multi-query reasoning  
- Build FastAPI interface  
- Add asynchronous execution  
- Extend to multi-agent collaboration  

---

## 🧠 Skills Demonstrated

- Object-Oriented Programming (OOP)  
- Modular software design  
- Retrieval-Augmented Generation (RAG)  
- Vector databases (FAISS)  
- NLP embeddings  
- Agent-based system design  

---

## 📌 Note

This project is a simplified implementation designed to demonstrate core concepts in RAG systems and agent-based architectures.

---

## 📜 License

MIT License
