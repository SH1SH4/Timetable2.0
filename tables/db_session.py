import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as env
from os import path
from dotenv import load_dotenv

DeclarativeBase = declarative_base()
__factory = None

dotenv_path = path.join(path.dirname(path.dirname(__file__)), '.env')
print(dotenv_path)
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)
DRIVERNAME = env.get('DB_DRIVERNAME')
HOST = env.get('DB_HOST')
PORT = int(env.get('DB_PORT'))
USERNAME = env.get('USER')
PASSWORD = env.get('PASSWORD')
DATABASE = env.get('DB')


def global_init():
    global __factory

    if __factory:
        return
    print(f'{DRIVERNAME}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4')
    engine = sa.create_engine(f'{DRIVERNAME}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4', pool_size=50, max_overflow=0)
    sess = sessionmaker(bind=engine)
    __factory = scoped_session(sess)
    DeclarativeBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()
