import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#app.config返回类字典对象，里面用来存放当前app实例的配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR, "../FlaskDirtory/manage_sys.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


# py文件配置方式
app.config.from_pyfile("settings")
app.config.from_object("config.DEBUG_CONFIG")



models = SQLAlchemy(app) #关联sqlalchemy和flask应用
