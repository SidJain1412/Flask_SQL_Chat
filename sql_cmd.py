from app import db
db.create_all()  # creates a .db file in project folder
# To add users, messages:
from app import User, Message
user_1 = User(username='Sid')
db.session.add(user_1)
msg_1 = Message(message='Test', sender=1)
db.session.add(msg_1)
db.session.commit()
# To get all
User.query.all()
# To get first
User.query.first()
# Get user by id
User.query.get(1)
# Drop the tables
db.drop_all()
# Backref example:
# User can send messages, do:
# messages = db.relationship('Message', backref='sentBy', lazy=True)
# now backref sentBy can be used on a message object to find the author of the message (__repr__ value of that user)
# lazy = True so it only loads when necessary