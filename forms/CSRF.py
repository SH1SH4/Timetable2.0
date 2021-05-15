from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from flask_wtf import FlaskForm
from dotenv import get_key
from os import path
from os import environ as env


dotenv_path = path.join(path.dirname(path.dirname(__file__)), '.env')
print(dotenv_path)
if path.exists(dotenv_path):
    CSRF_SECRET = get_key(dotenv_path, 'CSRF_SECRET')
else:
    CSRF_SECRET = env.get('CSRF_SECRET')


class MyBaseForm(FlaskForm):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
        csrf_time_limit = timedelta(minutes=20)