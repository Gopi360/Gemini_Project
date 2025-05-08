
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        break
    response = chat.sent_message(user_message)
    print("Gemini:", response.text)