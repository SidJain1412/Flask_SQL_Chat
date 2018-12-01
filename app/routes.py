from flask import render_template, request
from app.models import User, Message
from app import app


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/take_username', methods=["POST"])
def take_username():
    try:
        username = request.form['username']
        if username:
            return render_template('chat.html', username=username)
        else:
            return render_template('login.html')
    except Exception as e:
        return render_template('login.html')
