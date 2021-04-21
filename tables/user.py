from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
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
    token = Column(String, nullable=False)
    connection = Column(String, nullable=True)
    table = relationship("Tables")


class Tables(SqlAlchemyBase):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    day = Column(DateTime)
    time = Column(DateTime)
    homework_text = Column(Text)
    homework_img = Column(String)
    completed = Column(Boolean, default=False)
