from FlaskDirtory.main import models

db = models.session()

class BaseModel(models.Model):
    __abstract__ = True #抽象表为True 代表当前类为抽象类，不会创建表
    id = models.Column(models.Integer,primary_key=True,autoincrement=True)

    def save(self):
        db.add(self)
        db.commit()
    def delete_obj(self):
        db.delete(self)
        db.commit()

class User(BaseModel):   #学生表
    __tablename__ = "user"  #表名称
    username = models.Column(models.String(32))
    password = models.Column(models.String(32))
    identify = models.Column(models.Integer) #0 教师 1 学生

# if __name__ == '__main__':
#     models.create_all()

