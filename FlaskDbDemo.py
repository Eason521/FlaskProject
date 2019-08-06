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

class BaseModel(models.Model):
    __abstract__ = True #抽象表为True 代表当前类为抽象类，不会创建表
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)

    def save(self):
        session.add(self)
        session.commit()
    def delete_obj(self):
        session.delete(self)
        session.commit()

class Students(BaseModel):   #学生表
    __tablename__ = "students"  #表名称
    # id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer) #0 男 1 女 2 unknown


class Course(BaseModel): #课程
    __tablename__ = "course"
    # id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    label = models.Column(models.String(32))
    description = models.Column(models.Text)
    # stu_id = models.Column(models.Integer,models.ForeignKey(Student.id))

class Stu_Cou(BaseModel):
    __tablename__ = "stu_cou"
    # id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    course_id = models.Column(models.Integer,models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer,models.ForeignKey("students.id"))

class Grade(BaseModel):  #分数
    __tablename__ = "grade"
    # id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    grade = models.Column(models.Float, default=0)
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))
class Attendance(BaseModel):
    """
    考勤表，记录是否请假
    学员
    """
    __tablename__ = "attendance"
    # id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default = 1) #0 迟到  1 正常出勤  2 早退  3 请假  4 旷课
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))

class Teachers(BaseModel):
    """
    教师
    老师与课程是多对一关系
    """
    __tablename__ = "teachers"
    # id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer)  # 0 男 1女 -1 unknown
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))

# models.drop_all()
# models.create_all()
"""插入数据"""
# t1 = Teachers(name="小邓",age=28,gender=1,course_id=1)
# session.add(t1)
# session.commit()
#
# t2 = Teachers()
# t2.name ="小段"
# t2.age = 23
# t2.gender = 0
# t2.course_id = 1
# session.add_all([t1,t2])
# session.commit()

# course1 = Course()
# course1.label ="python"
# course1.description = "人生苦短，我用Python"
# course2 = Course()
# course2.label = "java"
# course2.description = "人生若短，我用java"
# course3 = Course()
# course3.label = "php"
# course3.description = "世界上最好的语言*_*"
#
# session.add_all([course1,course2,course3])
# session.commit()

"""查询数据"""
# teachers = Teachers.query.all()
# print(teachers)
# teachers = Teachers.query.first()
# print(teachers)

# teachers = Teachers.query.get(3)
# print(teachers)

# teachers = Teachers.query.filter_by(id=2).all()
# print(teachers)

# 排序
# teachers = Teachers.query.order_by("age").all()
# print(teachers)
# teachers = Teachers.query.order_by(models.desc("age")).all()
# print(teachers)

#offset 偏移量  limit 返回条数
# teachers = Teachers.query.offset(1).limit(2).all()
# print(teachers)

# """修改数据"""
# t = Teachers.query.get(1)
# print(t.name)
# t.name = "噔噔噔"
# session.add(t)
# session.commit()

"""删除数据"""

# t = Teachers.query.get(3)
# session.delete(t)
# session.commit()

"""结构优化后保存和删除数据"""
# t = Teachers()
# t.name="花花"
# t.age=26
# t.gender=1
# t.course_id=1
# t.save()

Teachers.query.get(1).delete_obj()

"""
Sqllite数据库，在整形的orm类型可以传入字符
如果是mysql数据库，插入非法类型，比如将字符插入整型，会直接插入0，并且进行waring警告
"""


