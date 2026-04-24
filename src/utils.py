def load_documents(path):
    with open(path, "r") as f:
        docs = f.readlines()
    return [d.strip() for d in docs if d.strip()]