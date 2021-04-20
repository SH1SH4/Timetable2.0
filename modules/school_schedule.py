from tables.user import User, Lessons
from tables import db_session


def lessons(form):
    db_sess = db_session.create_session()
    lesson = Lessons()
    lesson.day = form.day.data
    print(form.lesson1.data)
    print(form.lesson2.data)
    print(form.lesson3.data)
    print(form.lesson4.data)
    print(form.lesson5.data)
    lesson.lesson1 = form.lesson1.data
    lesson.lesson2 = form.lesson2.data
    lesson.lesson3 = form.lesson3.data
    lesson.lesson4 = form.lesson4.data
    lesson.lesson5 = form.lesson5.data
    lesson.lesson6 = form.lesson6.data
    lesson.lesson7 = form.lesson7.data
    lesson.lesson8 = form.lesson8.data
    # db_sess.add(lesson)
    # db_sess.commit()
    db_sess.close()