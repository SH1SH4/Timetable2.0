from json import loads, dumps, JSONDecodeError
from jsonschema import validate, ValidationError
from modules.schemas import LIST_SCHEMA, ADD_SCHEMA
from tables.user import User, Tables
from flask import Flask
from flask_restful import Resource, request
from tables import db_session


# class TableListResource(Resource):
#     def get(self, user_id):
#         db_sess = db_session.create_session()
#         user = db_sess.query(User).get(user_id)
#         try:
#             data = loads(request.get_data())
#             validate(instance=data,
#                      schema=LIST_SCHEMA)
#         except Exception:
#             response = Flask.response_class(status=400)
#             return response
#
#         try:
#             # Если не нашли курьера - выкидываем ошибку
#             if not user:
#                 response = Flask.response_class(status=404)
#                 return response
#             elif user.token != data['token']:
#                 response = Flask.response_class(status=405)
#                 return response
#             data =
#             response = Flask.response_class(status=400)
#             return response

class TableResource(Resource):
    def post(self, user_id):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        try:
            data = loads(request.get_data())
            validate(instance=data,
                     schema=ADD_SCHEMA)
        except AssertionError:
            return Flask.response_class(status=403)
        except Exception:
            response = Flask.response_class(status=400)
            return response
        data['owner_id'] = user_id
        table = Tables(data)
        db_sess.add(table)
        db_sess.commit()
        db_sess.close()
        response = Flask.response_class(status=400)
        return response


class ImgUpload(Resource):
        try:
            data = request.
        except Exception:
            response = Flask.response_class(status=400)
            return response
