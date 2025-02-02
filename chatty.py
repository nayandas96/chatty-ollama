import subprocess
import json
import os
import time

# CONFIG: Chat history file (so bot ain't forgetful)
HISTORY_FILE = "chat_history.json"

# CONFIG: Choose your AI model (download llama3 or other Ollama models first)
OLLAMA_MODEL = "llama3"  # Try "gemma", "mistral", etc.

def load_history():
    """Loads chat history from a JSON file. If none exists, it starts fresh."""
    return json.load(open(HISTORY_FILE, "r", encoding="utf-8")) if os.path.exists(HISTORY_FILE) else []

def save_history(history):
    """Saves chat history to a JSON file. Keeps the bot from being forgetful 🧠."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

def ollama_chat(prompt):
    """Talks to Ollama's local AI model and returns the response."""
    try:
        # Running Ollama with subprocess
        response = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL, prompt], 
            capture_output=True, text=True
        )

        # Extract AI output
        return response.stdout.strip()

    except Exception as e:
        return f"🚨 Error: {e} (bruh, something went wrong)"

def chatty_cli():
    """CLI chatbot that actually remembers convos & vibes with you 😎"""
    print("\n🤖 Chatty-Ollama Activated! Type 'exit' to yeet out.\n")

    chat_history = load_history()  # Load past convos
    
    while True:
        user_input = input("👤 You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 Chatty: Aight, see ya! 👋")
            break

        # Append user input to history
        chat_history.append({"role": "user", "content": user_input})

        # Get AI response from Ollama
        ai_message = ollama_chat(user_input)
        print(f"🤖 Chatty: {ai_message}\n")

        # Save AI response to history
        chat_history.append({"role": "assistant", "content": ai_message})
        save_history(chat_history)

if __name__ == "__main__":
    chatty_cli()  # Run that thing
