from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Time, Date
from sqlalchemy.orm import relationship
from .db_session import DeclarativeBase


class User(DeclarativeBase, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    surname = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(64), nullable=False)
    token = Column(String(128), nullable=False, unique=True)
    connection = Column(String(64), nullable=True)
    is_admin = Column(Boolean, default=False)
    is_ban = Column(Boolean, default=False)
    table = relationship("Tables",
                         order_by='Tables.day, Tables.time',
                         lazy='dynamic')
    images = relationship("Image", lazy='dynamic')
    # lessons = relationship("Lessons")


class Tables(DeclarativeBase):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    day = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    title = Column(String(64), nullable=False)
    homework_text = Column(Text(1024), nullable=True)  # Вы спросите, почему Homework_text а не просто text.
    homework_img = relationship('Image')  # Ответ прост - мы тупые
    completed = Column(Boolean, default=False)
    active = Column(Boolean, default=True)

    def to_dict(self):
        response = {
            "title": self.title,
            "day": str(self.day),
            "time": str(self.time),
        }
        if self.homework_text:
            response['homework_text'] = self.homework_text
        # if self.homework_img:
        #     response['homework_img'] = f"/picture/{self.homework_img[0].hash}"
        # Пикчи в Апиху обязательно когда-нибудь будут добавлены, правда-правда
        return response


class Image(DeclarativeBase):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    parent_table = Column(Integer, ForeignKey('homework.id'))
    hash = Column(String(128), unique=True)
