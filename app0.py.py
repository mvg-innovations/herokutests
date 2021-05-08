from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("ind.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(chatbot.get_response(user_text.lower()))


if __name__ == "__main__":
    app.run()
