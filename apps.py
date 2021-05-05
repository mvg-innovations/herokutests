from flask import Flask, render_template

app = Flask(__name__)

wsgi_app = app.wsgi_app


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5550'))
    except ValueError:
        PORT = 5550
    app.run(HOST, PORT)
