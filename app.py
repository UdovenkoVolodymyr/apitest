import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/messages', methods=['POST'])
def api_message():
    input_str = request.data.decode("utf-8")
    output_str = "Text Message: " + input_str
    return output_str
    #if request.headers['Content-Type'] == 'text/plain':
    #    return "Text Message: " + request.data


@app.route('/login', methods=['GET'])
def api_login():
    input = request.get_json()
    if input['login'] == 'admin' and input['password'] == '123':
        return '1'
    else:
        return '0'


if __name__ == '__main__':
    app.debug = True
    app.run()
