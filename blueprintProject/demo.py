
from flask import Flask
from flask import Blueprint

simple_blueprint = Blueprint("simple_page",__name__) #创建蓝图


# 蓝图路由和试图
@simple_blueprint.route("/")
def index():
    return "Hello world"

if __name__ == '__main__':
    app=Flask(__name__)
    app.register_blueprint(simple_blueprint) #注册
    app.run()