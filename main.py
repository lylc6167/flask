from flask import Flask, abort, request, jsonify
from config import DevConfig


app = Flask(__name__)

tasks = []

app.config.from_object(DevConfig)


@app.route('/')
def home():
    return '<h1>Hello world!</h1>'


if __name__ == "__main__":
    app.run()
