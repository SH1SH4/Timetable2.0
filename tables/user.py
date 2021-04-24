from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Time, Date
from sqlalchemy.orm import validates, relationship
from datetime import datetime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, nullable=False, unique=True)
    connection = Column(String, nullable=True)
    table = relationship("Tables",
                         order_by='Tables.day, Tables.time',
                         lazy='dynamic')
    images = relationship("Image", lazy='dynamic')
    # lessons = relationship("Lessons")


class Tables(SqlAlchemyBase):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    day = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    title = Column(String, nullable=False)
    homework_text = Column(Text, nullable=True)  # Вы спросите, почему Homework_text а не просто text.
    homework_img = relationship('Image')  # Ответ прост - мы тупые
    completed = Column(Boolean, default=False)
    active = Column(Boolean, default=True)

class Image(SqlAlchemyBase):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    parent_table = Column(Integer, ForeignKey('homework.id'))
    hash = Column(String, unique=True)
