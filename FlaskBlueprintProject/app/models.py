from app import models



class BaseModel(models.Model):
    __abstract__ = True #抽象表为True 代表当前类为抽象类，不会创建表
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)
    def save(self):
        db = models.session()
        db.add(self)
        db.commit()
    def delete_obj(self):
        db = models.session()
        db.delete(self)
        db.commit()

class User(BaseModel):   #学生表
    __tablename__ = "user"  #表名称
    username = models.Column(models.String(32))
    password = models.Column(models.String(32))
    identify = models.Column(models.String(32))


class Teachers(BaseModel):  #教师表
    __tablename__ = "teacher"
    username = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.String(32))
    course_id = models.Column(models.Integer,models.ForeignKey("course.id"))

class Students(BaseModel):   #学生表
    __tablename__ = "students"  #表名称
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer) #0 男 1 女 2 unknown


Stu_Cou = models.Table(
    "stu_cou",
    models.Column("id", models.Integer, primary_key=True, autoincrement=True),
    models.Column("course_id", models.Integer, models.ForeignKey("course.id")),
    models.Column("student_id", models.Integer, models.ForeignKey("students.id"))
)

class Course(BaseModel): #课程
    __tablename__ = "course"
    label = models.Column(models.String(32))
    description = models.Column(models.Text)

    to_teacher = models.relationship(
        "Teachers",   #映射表
        backref = "to_course_data" #反向映射字段，映射表通过该字段可以查到当前表内容
    )

    to_student = models.relationship(
        "Students",
        secondary = Stu_Cou,
        backref = models.backref("to_course",lazy="dynamic"),
        lazy = "dynamic",
        # lazy 的参数
            # select      访问该字段时候，加载所有的映射数据
            # joined      对关联的两个表students和stu_cou进行join查询
            # dynamic     不加载数据
    )

class Grade(BaseModel):  #分数
    __tablename__ = "grade"
    grade = models.Column(models.Float, default=0)
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))
class Attendance(BaseModel):
    """
    考勤表，记录是否请假
    学员
    """
    __tablename__ = "attendance"
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default = 1) #0 迟到  1 正常出勤  2 早退  3 请假  4 旷课
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))


# models.drop_all()
# # models.create_all()

