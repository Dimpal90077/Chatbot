from langchain_huggingface import HuggingFaceEmbeddings

embed = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello this is Akarsh Vyash",
    "Hello your name is Dimpal"
]

vectors = embed.embed_documents(texts)

print(vectors)