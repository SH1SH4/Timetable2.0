from hashlib import sha256
from tables.user import User
from tables import db_session


def reg(**kwargs):
    del kwargs['password_repeat']
    kwargs['password'] = sha256(kwargs['password'].encode('utf-8')).hexdigest()
    db_sess = db_session.create_session()
    print(kwargs)
    user = User(**kwargs)
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()