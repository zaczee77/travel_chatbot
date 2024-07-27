from flask import Flask, request, jsonify, send_from_directory # type: ignore
from chatbot import TravelChatbot

app = Flask(__name__)
chatbot = TravelChatbot()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json
    days = user_input.get('days')
    budget = user_input.get('budget')
    preferences = user_input.get('preferences')

    itinerary = chatbot.create_itinerary(days, budget, preferences)
    return jsonify(itinerary)

if __name__ == "__main__":
    app.run(debug=True)
