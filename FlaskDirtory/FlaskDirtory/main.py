import pymysql

from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect #CsrfProtect用于1.0以前版本

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

CSRFProtect(app)   #csrf使用



models = SQLAlchemy(app) #关联sqlalchemy和flask应用
