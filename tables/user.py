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
    table = relationship("Tables")
    # lessons = relationship("Lessons")


class Lessons(SqlAlchemyBase):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    day = Column(String, nullable=False)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    lesson1 = Column(String, nullable=True)
    lesson2 = Column(String, nullable=True)
    lesson3 = Column(String, nullable=True)
    lesson4 = Column(String, nullable=True)
    lesson5 = Column(String, nullable=True)
    lesson6 = Column(String, nullable=True)
    lesson7 = Column(String, nullable=True)
    lesson8 = Column(String, nullable=True)


class Tables(SqlAlchemyBase):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    day = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    title = Column(String, nullable=False)
    homework_text = Column(Text, nullable=True)
    homework_img = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
