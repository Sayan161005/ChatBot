"""Core chatbot logic: talks to a local Ollama model and remembers the chat."""

import ollama

MODEL_NAME = "gemma3:1b"

# Stores the entire conversation so the model has context
conversation = []


def ask_ai(message):
    """Send a message to the model and return its reply as a string."""
    conversation.append({"role": "user", "content": message})

    try:
        response = ollama.chat(model=MODEL_NAME, messages=conversation)
    except Exception as error:
        # Don't keep a message that never got an answer
        conversation.pop()
        return (
            "⚠️ Could not get a response from Ollama.\n"
            "Make sure Ollama is running and the model is installed:\n"
            f"    ollama pull {MODEL_NAME}\n\n"
            f"Details: {error}"
        )

    ai_reply = response["message"]["content"]
    conversation.append({"role": "assistant", "content": ai_reply})

    return ai_reply


def reset_conversation():
    """Forget everything said so far (used by 'New Chat')."""
    conversation.clear()
