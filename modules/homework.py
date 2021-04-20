from tables.user import Tables
from tables import db_session


def homework_form(form):
    db_sess = db_session.create_session()
    record = Tables()
    record.day = form.day.data
    record.time = form.time.data
    record.title = form.title.data
    record.homework_text = form.text.data
    # record.homework_img = form.file.data
    db_sess.add(record)
    db_sess.commit()
    db_sess.close()