import pymysql

from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect #CsrfProtect用于1.0以前版本
from flask_restful import Resource,Api

app=Flask(__name__)
pymysql.install_as_MySQLdb()

#app.config返回类字典对象，里面用来存放当前app实例的配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR, "../FlaskDirtory/manage_sys.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


# py文件配置方式
# app.config.from_pyfile("settings.py")

#类配置
app.config.from_object("config.DEBUG_CONFIG")

csrf=CSRFProtect(app)   #csrf使用
api=Api(app)   #关联接口和api插件

class Hello(Resource): #处理请求的视图类
    def get(self):
        return {"hello":"world"}

models = SQLAlchemy(app) #关联sqlalchemy和flask应用

api.add_resource(Hello,"/API/") #注册api接口路由
