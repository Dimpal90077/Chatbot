from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528"
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Write a paragraph on Data Science")

print(response)
print(response.content)
# print('Hello world')