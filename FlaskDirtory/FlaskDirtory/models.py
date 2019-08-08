from FlaskDirtory.main import models



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

class Course(BaseModel):   #课程
    __tablename__ = "course"
    course_name = models.Column(models.String(32))
    description = models.Column(models.Text)

class Teacher(BaseModel):  #教师表
    __tablename__ = "teacher"
    username = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.String(32))
    course_id = models.Column(models.Integer,models.ForeignKey("course.id"))

# models.drop_all()
# # models.create_all()

