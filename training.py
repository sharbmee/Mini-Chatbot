import json
import random
import nltk
from nltk.stem import WordNetLemmatizer


# Download if not already
nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

# Load intents.json
with open("intents.json", encoding="utf-8") as file:
    data = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if user_input in pattern.lower():
                return random.choice(intent["responses"])  # pick 1 response only
    
    return "Sorry, I didn’t understand that."

# Example loop
print("Chatbot is ready! (type 'quit' to exit)")

while True:
    message = input("You: ")
    if message.lower() == "quit":
        break
    print("Bot:", chatbot_response(message))
