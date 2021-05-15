from .CSRF import MyBaseForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField, DateField, FileField
from wtforms.validators import DataRequired


class HomeworkForm(MyBaseForm):
    title = StringField(validators=[DataRequired()])
    day = DateField(validators=[DataRequired()])
    time = TimeField(validators=[DataRequired()])
    text = TextAreaField()
    file = FileField('image')
    submit = SubmitField("Добавить")
