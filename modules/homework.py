from tables.user import Tables, Image
from tables import db_session
from os import getcwd, path, mkdir
from secrets import token_hex


def load_img(f, user, table, db_sess):
    exp = f.filename.split('.')[-1]
    filename = token_hex(16) + '.' + exp
    img = Image()
    img.owner_id = user
    img.parent_table = table
    img.hash = filename
    img.way = path.join('images', str(user))
    if not path.exists(path.join('static', img.way)):
        mkdir(path.join('static', img.way))
    f.save(path.join('static', img.way, filename))
    db_sess.add(img)
    db_sess.commit()


def homework_form(form, user):
    db_sess = db_session.create_session()
    record = Tables()
    record.day = form.day.data
    record.time = form.time.data
    record.title = form.title.data
    record.homework_text = form.text.data
    record.owner_id = user.id
    db_sess.add(record)
    db_sess.commit()
    f = form.file.data
    if f.filename:
        load_img(f, user.id, record.id, db_sess)
    db_sess.close()