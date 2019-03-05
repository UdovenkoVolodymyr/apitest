import requests
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/messages', methods=['GET'])
def api_message():
    input_str = request.data.decode("utf-8")
    #return "Text Message: " + input_str
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + input_str


if __name__ == '__main__':
    app.debug = True
    app.run()
