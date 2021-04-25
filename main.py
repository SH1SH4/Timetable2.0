import os

from flask import Flask, render_template, url_for, request, redirect, abort, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import Api
from forms.login import LoginForm
from forms.homework import HomeworkForm
from forms.register import RegisterForm
from modules.homework import homework_form
from forms.checkout import CheckoutForm
from modules.registration import reg
from modules.edit_homework import homework_edit
from modules.api import TableResource, TableListResource
from modules.login import login
from tables.user import User, Tables, Image
from tables import db_session
from secrets import token_urlsafe

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789qwerty'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)
api.add_resource(TableResource, "/add_work")
api.add_resource(TableListResource, "/homework_list")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect("/user")
    return render_template('welcome.html')


@app.route("/user")
def user():
    if current_user.is_authenticated:
        new_token = int(request.args.get('token', 0))
        if new_token:
            db_sess = db_session.create_session()
            current_user.connection = None
            current_user.token = token_urlsafe(16)
            db_sess.commit()
            return redirect("/user")
        else:
            return render_template(
                "user_cabinet.html",
                title="Личный кабинет",
                user=current_user)
    else:
        return redirect("/")


@app.route('/calendar', methods=["POST", "GET"])
def timetable():
    if request.method == "GET":
        return render_template('calendar.html')
    if request.method == "POST":
        return redirect('/login')


@app.route('/jsoncalendar')
def json_timetable():
    if current_user.is_authenticated:
        start = request.args.get('start')
        end = request.args.get('end')
        result = []
        db_sess = db_session.create_session()
        for obj in db_sess.query(Tables).filter(Tables.day.between(start, end)):
            print(type(obj.day))
            a = {
                'title': obj.title,
                'start': f"{obj.day}T{obj.time}",
                'url': url_for('school_schedule_num', number=obj.id)
            }
            if obj.completed:
                a['color'] = 'green'
            else:
                a['color'] = 'red'
            result.append(a)

        return jsonify(result)
    else:
        return redirect("/login")


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
        else:
            abort(404)
    else:
        return redirect("/")


@app.route("/homework", methods=["POST", "GET"])
def homework():
    form = HomeworkForm()
    if current_user.is_authenticated:
        if request.method == "GET":
            return render_template('add_homework.html', title="Запись", form=form)
        if request.method == "POST":
            homework_form(form, current_user)
            return redirect('/homework')
    else:
        return redirect("/")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        form = HomeworkForm()
        if request.method == "GET":
            record = db_sess.query(Tables).get(id)
            return render_template("edit_homework.html", title="Редактирование", form=form, table=record)
        if request.method == "POST":
            record = db_sess.query(Tables).get(id)
            homework_edit(form, record, current_user)
            return redirect(f"/school_schedule/{id}")


@app.route("/school_schedule", methods=["GET", "POST"])
def school_schedule():
    form = CheckoutForm()
    n = int(request.args.get('num', 1))
    if current_user.is_authenticated:
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
                table=list(current_user.table.filter(
                    Tables.completed == False,
                    Tables.active == True)
                )
            )
    else:
        return redirect("/")


@app.route("/archive", methods=["GET", "POST"])
def archive():
    form = CheckoutForm()
    n = int(request.args.get('num', 1))
    if current_user.is_authenticated:
        if request.method == "GET":
            return render_template(
                "archive.html",
                title="Расписание",
                form=form,
                n=n,
                user=current_user,
                table=list(current_user.table.filter(Tables.completed == True))
            )
    else:
        return redirect("/")


@app.route("/school_schedule/<int:number>", methods=["GET", "POST"])
def school_schedule_num(number):
    if current_user.is_authenticated:
        form = CheckoutForm()
        db_sess = db_session.create_session()
        if request.method == "GET":
            table = db_sess.query(Tables).get(number)
            if not table:
                abort(404)
            elif table.owner_id == current_user.id:
                return render_template(
                    "homework.html",
                    title=table.title,
                    user=current_user,
                    table=table,
                    form=form)
            else:
                abort(403)
        if request.method == "POST":
            if form.id.data == "delete":
                table = db_sess.query(Tables).get(number)
                db_sess.delete(table)
                db_sess.commit()
                return render_template("delete.html", title="Запись удалена")
            if form.id.data == "hide":
                table = db_sess.query(Tables).get(number)
                table.completed = True
                db_sess.commit()
                return render_template("text_archive.html", title="Добавлено в архив")
    else:
        return redirect("/")


@app.route('/registration', methods=["POST", "GET"])
def registration():
    form = RegisterForm()
    if request.method == "GET":
        return render_template('registration.html', form=form)
    if request.method == "POST":
        if form.password_repeat.data == form.password.data:
            reg(form)
            return redirect('/')
        else:
            return render_template('registration.html', form=form)


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