import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as env


DeclarativeBase = declarative_base()
__factory = None


DRIVERNAME = env.get('DRIVERNAME')
HOST = env.get('HOST')
PORT = int(env.get('PORT'))
USERNAME = env.get('USERNAME')
PASSWORD = env.get('PASSWORD')
DATABASE = env.get('DATABASE')


def global_init():
    global __factory

    if __factory:
        return

    engine = sa.create_engine(f'{DRIVERNAME}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4')
    __factory = sessionmaker(bind=engine)
    DeclarativeBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()
