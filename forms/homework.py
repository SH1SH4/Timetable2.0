from .CSRF import MyBaseForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField, DateField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class HomeworkForm(MyBaseForm):
    title = StringField(validators=[DataRequired()])
    day = DateField(validators=[DataRequired()])
    time = TimeField(validators=[DataRequired()])
    text = TextAreaField()
    file = FileField('image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField("Добавить")
