from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField, DateField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class HomeworkForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    day = DateField(validators=[DataRequired()])
    time = TimeField(validators=[DataRequired()])
    text = TextAreaField()
    file = FileField('image',  validators=[FileRequired(), FileAllowed([".png"], 'Images only!')])
    submit = SubmitField("Добавить")