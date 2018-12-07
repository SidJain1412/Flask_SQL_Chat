from flask import render_template, request, redirect, url_for
from app.views import verify_username, get_all_messages, add_message
from app import app
from flask import jsonify


@app.route('/')
def index(error=None):
    return render_template('login.html', error=error)


@app.route('/chat', methods=["POST"])
def take_username():
    try:
        username = request.form['username']
        if username:
            verify_username(username)
            messages = get_all_messages()
            return render_template('chat.html', username=username,
                                   messages=messages)
        else:
            return redirect(url_for('index'))
    except Exception as e:
        print(str(e))
        return redirect(url_for('index'))


@app.route('/test', methods=["GET"])
def test():
    data = {"message": "yooo"}
    print("Working")
    return jsonify(data)


@app.route('/send_message', methods=["GET", "POST"])
def send_message():
    message = request.form['message']
    if message:
        add_message(message)
    else:
        pass
    messages = get_all_messages()
    print(messages[-1])
    return jsonify(messages[-1])


@app.route('/get_last_message', methods=["GET"])
def get_last_message():
    message = get_all_messages()[-1]
    return jsonify(message)
