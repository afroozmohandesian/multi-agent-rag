from src.retriever import Retriever
from src.reasoner import Reasoner
from src.utils import load_documents

def main():
    docs = load_documents("data/docs.txt")

    retriever = Retriever(docs)
    reasoner = Reasoner()

    print("Multi-Agent RAG Assistant (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        retrieved_docs = retriever.retrieve(query)
        answer = reasoner.generate_answer(query, retrieved_docs)

        print("\nAgent Response:")
        print(answer)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()