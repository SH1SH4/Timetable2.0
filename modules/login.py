from hashlib import sha256
from flask_login import login_user
from tables.user import User
from tables import db_session


def login(mail, password):
    password = sha256(password.encode('utf-8')).hexdigest()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == mail)[0]
    login_user(user, remember=True)
    if user.password == password:
        return True
    return False
