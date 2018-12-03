from flask import render_template, request
from views import verify_username, get_all_messages
from app import app


@app.route('/')
def index(error=None):
    return render_template('login.html', error=error)


@app.route('/login', methods=["POST"])
def take_username():
    try:
        username = request.form['username']
        if username:
            verify_username(username)
            messages = get_all_messages()
            return render_template('chat.html', username=username,
                                   messages=messages)
        else:
            return render_template('login.html',
                                   error="Please enter a valid username")
    except Exception as e:
        print(str(e))
        return render_template('login.html')
