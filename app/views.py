from app import db
from app.models import User, Message


def verify_username(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()


def get_all_messages():
    return Message.query.all()
