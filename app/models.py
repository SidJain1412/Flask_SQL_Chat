from app import db


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
