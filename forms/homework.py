from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField, DateField, FileField


class HomeworkForm(FlaskForm):
    title = StringField()
    day = DateField()
    time = TimeField()
    text = TextAreaField()
    file = FileField()
    submit = SubmitField("Добавить")