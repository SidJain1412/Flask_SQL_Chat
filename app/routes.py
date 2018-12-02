from flask import render_template, request, jsonify, redirect
from app.models import User, Message
from app import app
from app import db


@app.route('/')
def index(error=None):
    return render_template('login.html', error=error)


@app.route('/login', methods=["POST"])
def take_username():
    try:
        username = request.form['username']
        if username:
            exists = User.query.filter_by(username=username).first()
            if not exists:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()
            return render_template('chat.html', username=username)
        else:
            return render_template('login.html',
                                   error="Please enter a valid username")
    except Exception as e:
        return render_template('login.html')
