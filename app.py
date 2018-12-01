from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/flask0.3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    messages = db.relationship('Message', backref='sentBy', lazy=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, message, sender):
        self.message = message
        self.sender = sender

    def __repr__(self):
        return '<Message %r>' % self.message


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/take_username', methods=["POST"])
def take_username():
    try:
        username = request.form['username']
        return render_template('chat.html', username=username)
    except Exception as e:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
