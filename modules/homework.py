from tables.user import Tables
from tables import db_session
from PIL import Image
from io import BytesIO


def load_img(img, user, table):
    pass


def homework_form(form, user):
    db_sess = db_session.create_session()
    record = Tables()
    record.day = form.day.data
    record.time = form.time.data
    record.title = form.title.data
    record.homework_text = form.text.data
    record.owner_id = user.id
    # record.homework_img = form.file.data
    Image.open(BytesIO(
    form.file.data.content)).show()
    db_sess.add(record)
    db_sess.commit()
    db_sess.close()