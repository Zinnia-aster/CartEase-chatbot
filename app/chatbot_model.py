import os
import pickle
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # this is app/
MODEL_DIR = os.path.join(BASE_DIR, '..', 'model')

MODEL_PATH = os.path.join(MODEL_DIR, 'chatbot_model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')
VECTORIZER_PATH = os.path.join(MODEL_DIR, 'vectorizer.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(ENCODER_PATH, 'rb') as f:
    label_encoder = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

def predict_intent(user_input):
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]
    intent = label_encoder.inverse_transform([prediction])[0]
    return intent



