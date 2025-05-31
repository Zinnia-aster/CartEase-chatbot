import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2') 

intent_responses = {
    'product_availability': [
        "Let me check if that's available for you!",
        "Yes, that product is in stock — ready to ship!",
        "It looks like the item is available. Would you like me to add it to your cart?",
        "That product is currently available. Need more info?"
    ],
    'payment_methods': [
        "We accept UPI, credit/debit cards, and net banking. What works best for you?",
        "You can pay using Paytm, Google Pay, or any major card.",
        "Multiple payment options are available — let me know your preference!",
        "Yes, we support UPI, cards, and even COD on some items!"
    ],
    'order_status': [
        "Can you please provide your order ID? I'll check it right away!",
        "You can track your order under 'My Orders', but I can help you here too!",
        "Checking your order... just a sec! What's your order number?",
        "Status update coming up! Please share your order ID."
    ],
    'cancel_order': [
        "Need to cancel? No problem. Just go to 'My Orders' and hit cancel.",
        "Orders can be cancelled before they ship — do you want help with that?",
        "You can cancel from your order page, or I can guide you through it.",
        "Tell me your order ID and I’ll help you cancel it."
    ],
    'shipping_info': [
        "Shipping usually takes 3-5 business days. Want express delivery?",
        "Standard delivery is quick, but we offer express options too!",
        "Where are you shipping to? I can give you better estimates!",
        "Most items ship within 48 hours. Need it faster?"
    ],
    'return_policy': [
        "Returns are easy! You have 30 days to return most items.",
        "We offer hassle-free returns. Need help with one?",
        "Check your order page for return options, or ask me here!",
        "Returning something? I'm here to help — what's the issue?"
    ]
}

intent_examples = {
    'product_availability': "Is this product available?",
    'payment_methods': "What payment methods do you accept?",
    'order_status': "Where is my order?",
    'cancel_order': "I want to cancel my order",
    'shipping_info': "How long does delivery take?",
    'return_policy': "Can I return this item?"
}

def generate_response(user_message: str):
    # Step 1: Embed user message and sample intent phrases
    user_embedding = model.encode([user_message])
    example_sentences = list(intent_examples.values())
    intent_labels = list(intent_examples.keys())
    example_embeddings = model.encode(example_sentences)

    # Step 2: Find best matching intent
    similarities = cosine_similarity(user_embedding, example_embeddings)[0]
    best_index = similarities.argmax()
    best_intent = intent_labels[best_index]

    # Step 3: Choose best response within that intent
    possible_responses = intent_responses[best_intent]
    response_embeddings = model.encode(possible_responses)
    response_similarities = cosine_similarity(user_embedding, response_embeddings)[0]
    best_response_index = response_similarities.argmax()

    return possible_responses[best_response_index]

if __name__ == "__main__":
    print("🛍️ Welcome to CartEase AI Shopping Assistant!")
    print("Type your message below (or 'exit' to quit):\n")

    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() == "exit":
            print("👋 Bye! Happy shopping!")
            break

        response = generate_response(user_input)
        print(f"🤖 CartEase Bot: {response}\n")
