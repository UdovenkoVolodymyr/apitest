import requests
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/messages', methods=['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data


if __name__ == '__main__':
    app.debug = True
    app.run()
