
from flask import Blueprint

simple_blueprint1 = Blueprint("simple_page1",__name__) #创建蓝图


# 蓝图路由和试图
@simple_blueprint1.route("/")
def index1():
    return "Hello world111111"
