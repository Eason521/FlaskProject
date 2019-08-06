import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#app.config返回类字典对象，里面用来存放当前app实例的配置
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"Demo.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

models = SQLAlchemy(app) #关联sqlalchemy和flask应用

class Student(models.Model):
    __tablename__ = "students"  #表名称
    id = models.Column(models.Integer,primary_key=True)
    name = models.Column(models.String(32),unique=True)
models.create_all()

@app.route('/')
def flaskdemo():
    return "我"

@app.route('/index/',methods=["GET","POST"])
def index():
    student_lists = [
        {"name":"张三","age":20,"phone":"13478272994"},
        {"name":"李四","age":14,"phone":"23423424322"},
        {"name":"王五","age":25,"phone":"23423453224"},
        {"name":"小六","age":26,"phone":"13353342442"},
        {"name":"阿七","age":17,"phone":"13344534538"},
    ]
    return render_template("index.html",student_lists=student_lists)

@app.route('/base/')
def base():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(debug=True)