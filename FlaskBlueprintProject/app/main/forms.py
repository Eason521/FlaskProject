import wtforms  #定义字段
from flask_wtf import FlaskForm #定义表单的父类
from wtforms import validators  #定义校验

#蓝图表单类不能查询数据库

class TeacherForm(FlaskForm):
    """
    form字段的参数
    label=None, 表单的标签
    validators=None, 校验，传入校验的方法
    filters=tuple(), 过滤
    description='',  描述
    id=None, html id
    default=None, 默认值
    widget=None,
    render_kw=None,
    """
    # course = Course.query.all()
    # cou_list = [(cou.id, cou.course_name) for cou in course]

    """表单类不能查询数据库，所以先手写类型，注意与数据库一致"""
    # list=[1,2,3,4,5,6]
    # cou_list = ["python","java","php","c","go","web"]
    name = wtforms.StringField("教师姓名",
                               render_kw = {
                                   "class": "form-control",
                                   "placeholder": "教师姓名",

                               },
                               validators = [
                                   validators.DataRequired("姓名不可以为空")
                               ]
    )
    age = wtforms.IntegerField("教师年龄",
                               render_kw={
                                   "class": "form-control",
                                   "placeholder": "教师年龄"
                               },
                               validators=[
                                   validators.DataRequired("年龄不可以为空")
                               ]
    )
    gender = wtforms.StringField("教师性别",
                                render_kw = {
                                    "class": "form-control",
                                    "placeholder": "教师性别"
                                },
                                validators=[
                                     validators.DataRequired("性别不可以为空")
                                ]
    )


class StudentForm(FlaskForm):

    name = wtforms.StringField("学生姓名",
                               render_kw = {
                                   "class": "form-control",
                                   "placeholder": "学生姓名",

                               },
                               validators = [
                                   validators.DataRequired("姓名不可以为空")
                               ]
    )
    age = wtforms.IntegerField("学生年龄",
                               render_kw={
                                   "class": "form-control",
                                   "placeholder": "学生年龄"
                               },
                               validators=[
                                   validators.DataRequired("年龄不可以为空")
                               ]
    )
    gender = wtforms.StringField("学生性别",
                                render_kw = {
                                    "class": "form-control",
                                    "placeholder": "学生性别"
                                },
                                validators=[
                                     validators.DataRequired("性别不可以为空")
                                ]
    )


