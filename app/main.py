from flask import Blueprint, request, jsonify,render_template
from app.response_generator import generate_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = generate_response(user_message)
    return jsonify({"response": bot_reply})

