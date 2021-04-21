from tables.user import Tables, Image
from tables import db_session
from os import getcwd, path, mkdir
from secrets import token_hex


def load_img(f, user, table):
    db_sess = db_session.create_session()
    exp = f.filename.split('.')[-1]
    filename = token_hex(16) + '.' + exp
    img = Image()
    img.owner_id = user.id
    img.parent_table = table.id
    img.hash = filename
    img.way = path.join(getcwd(), 'images', str(user.id))
    if not path.exists(img.way):
        mkdir(img.way)
    f.save(path.join(img.way, filename))
    db_sess.add(img)
    db_sess.commit()
    db_sess.close()


def homework_form(form, user):
    db_sess = db_session.create_session()
    record = Tables()
    record.day = form.day.data
    record.time = form.time.data
    record.title = form.title.data
    record.homework_text = form.text.data
    record.owner_id = user.id
    f = form.file.data
    if f.filename:
        load_img(f, user, record)
    db_sess.add(record)
    db_sess.commit()
    db_sess.close()