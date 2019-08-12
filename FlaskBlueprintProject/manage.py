from app import models,create_app
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from gevent import monkey


app = create_app("p ") #创建一个app

manager = Manager(app)

migrate = Migrate(app,models)
manager.add_command("db",MigrateCommand)


#大型项目优化多线程，小型项目时在app的__init__中直接优化

monkey.patch_all() #猴子补丁，将之前代码不契合协程的代码修改为契合
@manager.command
def runserver_gevent():
    from gevent import pywsgi
    server = pywsgi.WSGIServer(("127.0.0.1",5000),app)  #参数是url地址(ip,端口号)，启动应用
    server.serve_forever()


if __name__ == '__main__':
    manager.run()