# 🤖 Group 4 Interactive Chatbot System

This project is a terminal-based **Python chatbot** with multiple features packed into one interface. Built as a collaborative project, it simulates a smart assistant that can answer basic questions, generate passwords, and even entertain users with games like **Rock-Paper-Scissors** and **Coin Toss**.

## ✨ Features

- 💬 Responds to predefined questions using fuzzy matching
- 🔐 Generates secure passwords from your name
- 🕹️ Plays two interactive games:
  - Rock, Paper, Scissors
  - Coin Toss
- 🕒 Tells the current date and time
- 📚 Modular structure (separate Python files for logic)

## 🧠 Tech Stack

- **Language**: Python 3
- **Libraries Used**:
  - `random`
  - `datetime`
  - `difflib` (for fuzzy matching in chatbot responses)
  - `input` / `print` for CLI interaction

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/M-sudais/Group4-Chatbot.git
cd Group4-Chatbot
python chatbot.py```

🔧 Project Structure
📁 Group4-Chatbot/
├── chatbot.py              # Main chatbot logic and interface
├── chatbotdictionaries.py  # Dictionary of responses
├── rock_paper_scissors.py  # Rock-paper-scissors game
├── generate_password.py    # Password generator
└── coin_toss_game.py       # (integrated directly in main for now)

💡 Future Improvements (Phase 2 Ideas)
- 💾 Add persistent memory (save user queries and game stats to a file)
- 🌐 Let the chatbot answer real-time questions using API (e.g., weather, news)
- 🎨 Build a GUI using Tkinter or PyQt
- 🔊 Add text-to-speech capabilities for responses
- 🧠 Train it with NLP techniques using nltk or transformers
👨‍💻 Author
Built with passion by msudais and his internship team

📄 License
This project is open-source and available for educational use. Contributions are welcome!









