from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField, DateField, FileField
from wtforms.validators import DataRequired


class HomeworkForm(FlaskForm):
    title = StringField()
    day = DateField()
    time = TimeField()
    text = TextAreaField()
    file = FileField()
    submit = SubmitField("Добавить")