
from flask import Blueprint

simple_blueprint2 = Blueprint("simple_page2",__name__) #创建蓝图


# 蓝图路由和试图
@simple_blueprint2.route("/index2/")
def index2():
    return "Hello world2222222222"