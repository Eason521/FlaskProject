from flask import Flask
from flask_script import Manager

from flask import Blueprint

app = Flask(__name__)



simple_blueprint1 = Blueprint("simple_page1",__name__) #创建蓝图


# # 蓝图路由和视图
@simple_blueprint1.route("/")
def index1():
    return "Hello world111111"
app.register_blueprint(simple_blueprint1)
manager = Manager(app) #app命令行序列化

@manager.command
def hello(name = "creat_add_user"):
    username = input("username :")
    password = input("password :")
    email = input("email :")










if __name__ == '__main__':
    manager.run()

"""
命令行启动
python manage.py runserver
"""