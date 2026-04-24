class Reasoner:
    def __init__(self):
        pass

    def generate_answer(self, query, context_docs):
        context = " ".join(context_docs)

        response = f"""
Query: {query}

Context:
{context}

Answer:
Based on the retrieved information, this situation relates to environmental hazards.
Preventive measures and monitoring systems are recommended.
"""
        return response.strip()