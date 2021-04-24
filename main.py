from flask import Flask, render_template, url_for, request, redirect, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from modules.api import TableResource
from flask_restful import Api
from forms.login import LoginForm
from forms.homework import HomeworkForm
from forms.register import RegisterForm
from modules.homework import homework_form
from  forms.checkout import CheckoutForm
from modules.registration import reg
from tables.user import User, Tables, Image
from modules.login import login
from tables import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789qwerty'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)
api.add_resource(TableResource)


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
        return render_template(
            "user_cabinet.html",
            title="Личный кабинет",
            user=current_user)
    else:
        abort(403)


@app.route('/calendar', methods=["POST", "GET"])
def timetable():
    if request.method == "GET":
        return render_template('calendar.html')
    if request.method == "POST":
        return redirect('/')


@app.route('/picture/<hash>')
def picture(hash):
    if current_user.is_authenticated:
        pics = current_user.images
        pic = pics.filter(Image.hash == hash)[0]
        if pic:
            user_id = str(current_user.id)
            return f'''<p><img src="{url_for('static',
                filename='images' + '/' + user_id + '/' + pic.hash)}"
style="margin: 2rem; width: 100%;"
                                class="rounded mx-auto d-block">'''


@app.route("/homework", methods=["POST", "GET"])
def homework():
    form = HomeworkForm()
    if current_user.is_authenticated:
        if request.method == "GET":
            return render_template('add_homework.html', title="Запись", form=form)
        if request.method == "POST":
            homework_form(form, current_user)
            return redirect('/')
    else:
        return redirect("/registration")


@app.route("/school_schedule", methods=["GET", "POST"])
def school_schedule():
    form = CheckoutForm()
    n = request.args.get('num')
    if not n:
        n = 1
    else:
        n = int(n)
    if current_user.is_authentificated:
        if request.method == "GET":
            return render_template(
                "school_schedule.html",
                title="Расписание",
                form=form,
                n=n,
                user=current_user,
                table=list(current_user.table.filter(Tables.completed == False))
            )
        if request.method == "POST":
            db_sess = db_session.create_session()
            record = current_user.table.filter(Tables.id == form.id.data)[0]
            record.completed = True
            db_sess.commit()
            return render_template(
                "school_schedule.html",
                title="Расписание",
                user=current_user,
                n=n,
                form=form,
                table=list(current_user.table.filter(Tables.completed == False, Tables.active == True))
            )
    else:
        return redirect("/registration")


@app.route("/archive", methods=["GET", "POST"])
def archive():
    form = CheckoutForm()
    if current_user.is_authentificated:
        if request.method == "GET":
            return render_template(
                "archive.html",
                title="Расписание",
                form=form,
                user=current_user,
                table=list(current_user.table.filter(Tables.completed == True, Tables.active == True))
            )
    else:
        return redirect("/registration")


@app.route("/school_schedule/<int:number>", methods=["GET"])
def school_schedule_num(number):
    if current_user.is_authentificated:
        db_sess = db_session.create_session()
        if request.method == "GET":
            table = db_sess.query(Tables).get(number)
            if table and table.owner_id == current_user.id:
                return render_template(
                    "homework.html",
                    title=table.title,
                    user=current_user,
                    table=table)
            else:
                abort(403)
    else:
        return redirect("/registration")


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