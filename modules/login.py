from hashlib import sha256
from tables.user import User
from tables import db_session


def login(mail, password):
    password = sha256(password.encode('utf-8')).hexdigest()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == mail)[0]
    if user.password == password:
        return True
    return False
