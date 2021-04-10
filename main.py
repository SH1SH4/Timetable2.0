from flask import Flask
from data import db_session
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



def main():
    app.run(host='0.0.0.0', port=8080, threaded=True)
    db_session.global_init('db/homework.db')


if __name__ == '__main__':
    main()