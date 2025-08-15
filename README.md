# 🤖 AI Chatbot

A simple AI-powered chatbot built with **Python**, **TensorFlow/Keras**, and **NLTK**.  
The chatbot uses a training dataset (`intents.json`) that contains predefined patterns and responses to simulate conversations.

---

## ✨ Features
- Responds to user queries based on trained intents.
- Easy to customize by editing `intents.json`.
- Lightweight and beginner-friendly project.
- Extendable for real-world applications (FAQ bots, personal assistants, etc.).

---

## 📂 Project Structure
```
AI-Chatbot/
│── intents.json       # Training data for chatbot (intents, patterns, responses)
│── training.py        # Script to train the chatbot model
│── chatbot.py         # Main file to run the chatbot
│── README.md          # Project documentation
```

---

## ⚙️ Installation
Clone this repository:
```bash
git clone https://github.com/your-username/Mini-Chatbot.git
cd AI-Chatbot
```

Install dependencies:
```bash
pip install tensorflow nltk numpy
```

Download NLTK data (only once):
```python
import nltk
nltk.download('punkt')
```

---

## ▶️ Usage
1. Train the model:
   ```bash
   python training.py
   ```

2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

---

## 📌 Example Intents
```json
{
  "tag": "greetings",
  "patterns": ["hello", "hi", "hey", "namaste", "salaam"],
  "responses": ["Hello!", "Hi there 👋", "Hey! How can I help you?"]
}
```

---

## 🚀 Future Improvements
- Add more intents for broader conversation coverage.
- Create a web-based interface (Flask/Django + React).
- Integrate with APIs (Weather, News, Wikipedia, etc.).
- Deploy on cloud platforms (Heroku, Vercel, etc.).

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📝 License
This project is licensed under the **MIT License** – free to use and modify.
