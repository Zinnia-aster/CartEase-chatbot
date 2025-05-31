import os
import pickle
import numpy as np

# Define paths to the saved models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # this is app/
MODEL_DIR = os.path.join(BASE_DIR, '..', 'model')

MODEL_PATH = os.path.join(MODEL_DIR, 'chatbot_model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')
VECTORIZER_PATH = os.path.join(MODEL_DIR, 'vectorizer.pkl')

# Load the trained chatbot model
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# Load the label encoder
with open(ENCODER_PATH, 'rb') as f:
    label_encoder = pickle.load(f)

# Load the TF-IDF vectorizer
with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

# Function to predict intent from user input
def predict_intent(user_input):
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]
    intent = label_encoder.inverse_transform([prediction])[0]
    return intent

# Optional: test it directly
if __name__ == '__main__':
    test_input = "cancel my order"
    
    print("User said:", test_input)
    print("Predicted intent:", predict_intent(test_input))


