from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.login import LoginForm
from forms.register import RegisterForm
from modules.registration import reg
from tables.user import User
from modules.login import login
from tables import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789qwerty'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    form = User()
    return render_template('main.html', form=form)
    return render_template('page1.html')


@app.route('/registration', methods=["POST", "GET"])
def registration():
    form = RegisterForm()
    if request.method == "GET":
        return render_template('registration.html', form=form)
    if request.method == "POST":
        reg(form)
        return redirect('/')


@app.route("/login", methods=["POST", "GET"])
def authorization():
    form = LoginForm()
    if request.method == "GET":
        return render_template('authorization.html', form=form)
    if request.method == "POST":
        if login(form.email.data, form.password.data):
            return redirect("/")
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
    app.run(debug=True)