from . import api
from flask_restful import Resource

@api.resource("/hello/")
class Hello(Resource):
    def get(self):
        return {"hello":"world"}
