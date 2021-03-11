from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    py = 'I Love Python'
    return py
