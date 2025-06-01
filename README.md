# 🛍️ CartEase Chatbot

**CartEase** is a stylish AI-powered shopping assistant built with Python, Flask, and NLTK. It provides a smooth chat experience where users can ask shopping-related questions and get instant responses in a clean, interactive UI.

---

## ✨ Features

- 🤖 AI chatbot using NLTK & basic ML
- 🌐 Flask backend with a real-time chat UI
- 💬 User-friendly conversation experience
- 🎨 Responsive and professional-looking web page
- 📦 Modular and easy to customize

---

## 📁 Project Structure

CartEase-chatbot/
├── app/
│   ├── __init__.py               # Initializes Flask app
│   ├── chatbot_model.py          # NLP model & training (if used)
│   ├── main.py                   # Chat routes and logic
│   ├── response_generator.py     # Predicts bot's response
│   ├── templates/
│   │   └── index.html            # Main chat interface
│   ├── static/
│   │   └── style.css             # Styling for the chatbot page
│   └── __pycache__/              # Python cache files
├── run.py                        # Main entry point to run the Flask app
├── intents.json                  # Contains intents and responses
└── README.md                     # You're here!

---

## 💡 Tech Stack
Frontend: HTML, CSS (custom), AJAX (for message sending)

Backend: Python, Flask

NLP: NLTK (Natural Language Toolkit)


## 🧠 Chatbot Logic
Training: Uses intents with patterns and responses (chatbot_model.py)

Tokenization & Lemmatization: For preprocessing user input

Bag of Words: Converts sentences to numerical input

Model: Trained with a basic neural net (or rule-based matching)

Response Matching: Logic lives in response_generator.py


## ✨ Customization Ideas
Add more intents to increase chatbot intelligence

Integrate with a real product database or API

Add login/authentication

Deploy it on platforms like Render, Vercel, or Heroku

Add voice interaction using Web Speech API

## 👩‍💻 Made With Love By
Priya (a.k.a Zinnia 🌸)
