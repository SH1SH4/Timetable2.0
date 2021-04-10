from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import validates, relationship
from datetime import datetime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    mail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    table = relationship("tables")


class Tables(SqlAlchemyBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    day = Column(DateTime)
    time = Column(DateTime)
    homework_text = Column(Text)
    homework_img = Column(String)
