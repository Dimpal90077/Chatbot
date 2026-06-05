from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage


model= ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)
message=[ SystemMessage(content="you are a angry AI agent")]

# messages = [
#     (
#         "system",
#         "You are a helpful assistant.",
#     ),
#     ("human", "whrite a poem on data science?"),
# ]


#  ye use tb krenge jb tk hmra conversation khatam na ho jaye
#  jo bhi conversation hai uso saved krne ke liye append apply krte hai
# chat history ko save krne ke liye model me messge ko direct invoke kr rhe hai

print("-----------Conversation B/w Adarsh & Dimpal----------")
while True:
    prompt=input("you:")

    message.append(HumanMessage(content=prompt))
    if(prompt==0):
        break
    # response= model.invoke(prompt)
    response= model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Adarsh:",response.content)


# from langchain_groq import ChatGroq
# from langchain.messages import HumanMessage

# llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe this image in detail."},
#         {
#             "type": "image_url",
#             "image_url": {"url": "https://example.com/image.jpg"},
#         },
#     ]
# )

# response = llm.invoke([message])
# print(response.content)


