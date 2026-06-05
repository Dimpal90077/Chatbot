# 🤖 Emotion AI Chatbot

An interactive AI chatbot built using Streamlit, LangChain, and Mistral AI that can respond with different emotional personalities.

## 🌐 Live Demo

https://chatbot-h8mwzuoyvdwpfirekr8blc.streamlit.app/

## ✨ Features

- 😊 Happy AI Mode
- 😢 Sad AI Mode
- 😡 Angry AI Mode
- 😂 Joke AI Mode
- Interactive chat interface
- Real-time AI responses
- Session-based conversation history
- Clean and user-friendly Streamlit UI

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Python Dotenv

## 📂 Project Structure

```text
Chatbot/
│
├── chatmodels/
│   └── uichatbot.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Dimpal90077/Chatbot.git
cd Chatbot
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add API Key

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run chatmodels/uichatbot.py
```

## 🎭 Available Personalities

| Mode | Behavior |
|--------|----------|
| 😊 Happy | Cheerful and positive responses |
| 😢 Sad | Emotional and gloomy responses |
| 😡 Angry | Aggressive and angry responses |
| 😂 Joke | Funny and humorous responses |

## 📸 Screenshot

Add your project screenshots here.

## 🔮 Future Improvements

- Chat export feature
- Dark/Light theme toggle
- Voice interaction
- Multiple AI model support
- Chat history database

## 👩‍💻 Developer

**Dimpal Singh**

GitHub: https://github.com/Dimpal90077

LinkedIn: https://www.linkedin.com/in/dimpal-singh-8449862a3

---

⭐ If you like this project, consider giving it a star!
