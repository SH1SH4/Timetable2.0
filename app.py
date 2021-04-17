from flask import Flask, render_template, url_for, request
from modules.registration import reg
from modules.login import login
from tables import db_session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page1.html')


@app.route('/registration', methods=["POST", "GET"])
def registration():
    if request.method == "GET":
        return render_template('registration.html')
    if request.method == "POST":
        form = request.form.to_dict()
        reg(**form)
        return "OK"


@app.route("/login", methods=["POST", "GET"])
def authorization():
    if request.method == "GET":
        return render_template('authorization.html')
    if request.method == "POST":
        if login(request.form.get('email'), request.form.get('password')):
            return "OK"
        return "NOT OK"


@app.route('/timetable', methods=["POST", "GET"])
def timetable():
    if request.method == "GET":
        print(1)
        return render_template('calendar.html')
    if request.method == "POST":
        print(2)
        return '2'


if __name__ == "__main__":
    db_session.global_init('db/db.db')
    app.run()