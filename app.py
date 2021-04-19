from flask import Flask, render_template, url_for, request, redirect, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.login import LoginForm
from forms.register import RegisterForm
from modules.school_schedule import lessons
from forms.school_schedule import ScheduleForm
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
    return render_template('main.html')


@app.route("/user")
def user():
    if current_user.is_authenticated:
        return render_template("user_cabinet.html", title="Личный кабинет", user=current_user)
    else:
        abort(404)


@app.route("/school_schedule", methods=["GET", "POST"])
def school_schedule():
    form = ScheduleForm()
    if request.method == "GET":
        return render_template("school_schedule.html", title="Расписание", form=form)
    if request.method == "POST":
        lessons(form)
        return redirect("/")


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
        return render_template('authorization.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init('db/db.db')
    app.run(port=8080, debug=True)