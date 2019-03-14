import os
import time
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Auth


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/messages', methods=['POST'])
def api_message():
    input_str = request.data.decode("utf-8")
    output_str = "Text Message: " + input_str
    return output_str
    # if request.headers['Content-Type'] == 'text/plain':
    #    return "Text Message: " + request.data


@app.route('/login', methods=['GET'])
def api_login():
    input = request.get_json()
    if input['login'] == 'admin' and input['password'] == '123':
        return '1'
    else:
        return '0'


# =====================================================================

@app.route("/add")
def add_book():
    name = request.args.get('name')
    author = request.args.get('author')
    published = request.args.get('published')
    try:
        book = Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
        return (str(e))


@app.route("/getall")
def get_all():
    try:
        books = Book.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
        return (str(e))


@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        outh = Auth.query.filter_by(id=id_).first()
        return jsonify(outh.serialize())
    except Exception as e:
        return (str(e))


@app.route("/add/form", methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        try:
            outh = Auth(
                login=login,
                password=password,
                birthday=birthday,
		email=email,
		timestamp=int(time.time())
            )
            db.session.add(outh)
            db.session.commit()
            return "Book added. book id={}".format(outh.id)
        except Exception as e:
            return (str(e))
    return render_template("getdata.html")


if __name__ == '__main__':
    # app.debug = True
    app.run()
