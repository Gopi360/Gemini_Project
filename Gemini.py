import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set it in the .env file.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        break
    response = chat.send_message(user_message)
    print("Gemini:", response.text)