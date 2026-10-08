"""Command-line version of the chatbot (with conversation memory)."""

from chatbot import ask_ai, MODEL_NAME

print(f"🤖 AI ChatBot is running! (model: {MODEL_NAME})")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip()

    if user.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    if user == "":
        continue

    print("Bot:", ask_ai(user))
