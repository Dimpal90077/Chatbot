# import os
# from dotenv import load_dotenv

# load_dotenv()

# print("Google:", bool(os.getenv("GOOGLE_API_KEY")))
# print("OpenAI:", bool(os.getenv("OPENAI_API_KEY")))
# print("Groq:", bool(os.getenv("GROQ_API_KEY")))
# print("Mistral:", bool(os.getenv("MISTRAL_API_KEY")))

from dotenv import load_dotenv
import os

load_dotenv()

print("HuggingFaceHub:", bool(os.getenv("HUGGINGFACEHUB_API_KEY")))