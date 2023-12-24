from flask import Flask, render_template, request, jsonify
from chat import get_response  # Import your chatbot logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = get_response(user_text)
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)
