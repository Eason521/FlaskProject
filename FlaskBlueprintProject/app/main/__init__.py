from flask import Blueprint

from flask_restful import Api

#实例化蓝图
main = Blueprint("main",__name__)

api = Api(main)

from . import views
from . import ApiResource