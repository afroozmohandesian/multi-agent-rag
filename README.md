# 🤖 Multi-Agent RAG Assistant

## 🧠 Overview
This project implements a multi-agent Retrieval-Augmented Generation (RAG) system with a modular architecture.

Instead of relying on a single model, the system separates responsibilities into independent agents:
- Retriever Agent → retrieves relevant documents from a knowledge base  
- Reasoner Agent → generates answers based on retrieved context  

This project demonstrates core concepts in agent-based AI systems, modular reasoning, and knowledge retrieval pipelines.

---

## ✨ Features
- Vector search using FAISS  
- Embeddings via SentenceTransformers  
- Modular agent-based design  
- Context-aware response generation  
- Lightweight and extensible architecture  

---


## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
🧪 Example
You: What causes floods?

Agent:
Based on the retrieved information, floods often occur due to heavy rainfall and poor drainage systems.
⚙️ Architecture
User Query
    ↓
Retriever Agent
    ↓
Relevant Documents
    ↓
Reasoner Agent
    ↓
Final Answer
🚀 Future Improvements
Integrate real LLMs (OpenAI / local models)
Add multi-query reasoning
Build FastAPI interface
Add asynchronous execution
Extend to multi-agent collaboration
📌 Note

This project is a simplified implementation designed to demonstrate core concepts in RAG systems and agent-based architectures.
