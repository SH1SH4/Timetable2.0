from .CSRF import MyBaseForm
from wtforms import SubmitField, StringField


class CheckoutForm(MyBaseForm):
    id = StringField()
    submit = SubmitField("Выполнить")
    delete = SubmitField("Удалить")
