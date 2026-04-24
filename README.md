# 🤖 Multi-Agent RAG Assistant

## Overview
This project implements a simple multi-agent Retrieval-Augmented Generation (RAG) system.

It separates responsibilities into:
- Retriever Agent → fetch relevant documents
- Reasoner Agent → generate answers based on context

## Features
- Vector search using FAISS
- Embeddings via SentenceTransformers
- Modular agent design

## Run

```bash
python main.py

Example

You: What causes floods?
Agent: Based on retrieved information...


Architecture

Retriever → Context → Reasoner → Answer
