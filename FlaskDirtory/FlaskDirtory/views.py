from FlaskDirtory.models import Students, Course, Teachers

"""插入数据"""
# t1 = Teachers(name="小邓",age=28,gender=1,course_id=1)
# session.add(t1)
# session.commit()
# #
# t2 = Teachers()
# t2.name ="小段"
# t2.age = 23
# t2.gender = 0
# t2.course_id = 1
# session.add_all([t1,t2])
# session.commit()
#
# course1 = Course()
# course1.label ="python"
# course1.description = "人生苦短，我用Python"
# course2 = Course()
# course2.label = "java"
# course2.description = "人生若短，我用java"
# course3 = Course()
# course3.label = "php"
# course3.description = "世界上最好的语言*_*"
# #
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


# s = Students()
# s.name = '张三'
# s.age = 20
# s.gender = 1
# s.save()
# s = Students()
# s.name = '李四'
# s.age = 18
# s.gender = 0
# s.save()
#
# g1 = Grade()
# g1.grade = 80
# g1.course_id = 1
# g1.student_id = 1
# g1.save()
#
# g2 = Grade()
# g2.grade = 75
# g2.course_id = 2
# g2.student_id = 1
# g2.save()
#
# g3 = Grade()
# g3.grade = 75
# g3.course_id = 3
# g3.student_id = 1
# g3.save()
#
# g4 = Grade()
# g4.grade = 82
# g4.course_id = 1
# g4.student_id = 2
# g4.save()










# Teachers.query.get(1).delete_obj()

"""
Sqllite数据库，在整形的orm类型可以传入字符
如果是mysql数据库，插入非法类型，比如将字符插入整型，会直接插入0，并且进行waring警告
"""

"""一对多映射查询"""
t = Teachers.query.get(1)
print(t.to_course_data)

c = Course.query.get(1)
print(c.to_teacher)

"""多对多映射查询"""
student = Students.query.get(1)
print(student)
print(student.to_course.all()) #查询学员id为1的所有课程

course = Course.query.get(1)
print(course.to_student.all()) #查询课程id为1的所有有学员