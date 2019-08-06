import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#app.config返回类字典对象，里面用来存放当前app实例的配置
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"manage_sys.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

models = SQLAlchemy(app) #关联sqlalchemy和flask应用

session = models.session()

class Students(models.Model):   #学生表
    __tablename__ = "students"  #表名称
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer) #0 男 1 女 2 unknown


class Course(models.Model): #课程
    __tablename__ = "course"
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    label = models.Column(models.String(32))
    description = models.Column(models.Text)
    # stu_id = models.Column(models.Integer,models.ForeignKey(Student.id))

class Stu_Cou(models.Model):
    __tablename__ = "stu_cou"
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    course_id = models.Column(models.Integer,models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer,models.ForeignKey("students.id"))

class Grade(models.Model):  #分数
    __tablename__ = "grade"
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    grade = models.Column(models.Float, default=0)
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))
class Attendance(models.Model):
    """
    考勤表，记录是否请假
    学员
    """
    __tablename__ = "attendance"
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default = 1) #0 迟到  1 正常出勤  2 早退  3 请假  4 旷课
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))

class Teachers(models.Model):
    """
    教师
    老师与课程是多对一关系
    """
    __tablename__ = "teachers"
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer)  # 0 男 1女 -1 unknown
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))

# models.drop_all()
# models.create_all()

t1 = Teachers(name="小邓",age=28,gender=1,course_id=1)
session.add(t1)
session.commit()

t2 = Teachers()
t2.name ="小段"
t2.age = 23
t2.gender = 0
t2.course_id = 1
session.add_all([t1,t2])
session.commit()

