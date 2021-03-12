from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() -> str:
    py = 'I Love Python'
    return py


@app.route('/<message>')
def echoMessage(message: str) -> str:
    py = 'I Love Python from:'
    return py + message
