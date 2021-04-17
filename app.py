from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
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
            return redirect("/")
        return "NOT OK"


if __name__ == "__main__":
    db_session.global_init('db/db.db')
    app.run()