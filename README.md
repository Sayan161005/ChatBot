# 🤖 My AI ChatBot

A desktop AI chatbot that runs **fully offline** on your own machine. It uses [Ollama](https://ollama.com) to run Google's **Gemma 3** model locally, with a modern dark-themed chat interface built in Tkinter.

No API keys, no cloud, no cost: your conversations never leave your computer.

## ✨ Features

- 💬 Chat bubbles: your messages on the right, the AI's on the left
- 🌙 Dark theme
- 🧠 Conversation memory: the AI remembers what you said earlier in the chat
- ⚡ Responsive UI: the AI runs in a background thread, so the window never freezes
- 📜 Scrollable chat history (mouse wheel works on Windows, macOS and Linux)
- 🆕 **File → New Chat** clears the screen and the AI's memory
- 🖥️ Also includes a simple command-line version

## 🛠️ Tech Stack

- Python 3.9+
- Tkinter (GUI)
- Ollama (local model runtime)
- Gemma 3 (`gemma3:1b`)

## 📦 Prerequisites

1. **Python 3.9 or newer**. Tkinter ships with the standard Python installer. On some Linux distros install it with `sudo apt install python3-tk`.
2. **Ollama**: download it from [ollama.com/download](https://ollama.com/download).
3. **The Gemma 3 model**:
   ```bash
   ollama pull gemma3:1b
   ```

## 🚀 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Sayan161005/ChatBot.git
cd ChatBot

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make sure Ollama is running, then launch the app
python app.py
```

Prefer the terminal? Run the CLI version instead (type `bye` to exit):

```bash
python cli.py
```

## 📁 Project Structure

```
.
├── app.py             # Tkinter GUI (dark theme, chat bubbles)
├── chatbot.py         # Core logic: Ollama calls + conversation memory
├── cli.py             # Command-line version
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## ⚙️ Configuration

To use a different model, change `MODEL_NAME` in `chatbot.py` (after running `ollama pull <model>`):

```python
MODEL_NAME = "gemma3:4b"
```

Bigger models give better answers but need more RAM.

## 🩺 Troubleshooting

| Problem | Fix |
|---|---|
| "Could not get a response from Ollama" | Start the Ollama app/service and check that it's running |
| Model not found | Run `ollama pull gemma3:1b` |
| `No module named tkinter` (Linux) | `sudo apt install python3-tk` |
| Slow replies | Normal on CPU-only machines; try a smaller model or close other apps |

## 🔮 Future Improvements

- Streaming responses (word-by-word output)
- Save and load chat history
- Model selector in the UI
- Light/dark theme toggle

## 👤 Author

**SAYAN SAHA**

- GitHub: [@Sayan161005](https://github.com/Sayan161005)

⭐ If you found this project helpful, consider giving it a star!