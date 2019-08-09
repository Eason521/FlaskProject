from flask import Blueprint

#实例化蓝图
main = Blueprint("main",__name__)

from . import views