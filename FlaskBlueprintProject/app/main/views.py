import hashlib

from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import make_response
from flask import session
from .. import cache

from . import main
from app import csrf
from  app.main.forms import TeacherForm  #表单类使用
from  app.main.forms import StudentForm  #表单类使用
from app.models import *

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

def loginValid(fun):
    def inner(*args,**kwargs):
        cookie_username = request.cookies.get("username")
        cookie_user_id = request.cookies.get("user_id")
        session_username = session.get("username")
        if cookie_username and cookie_user_id and session_username:
            if cookie_username == session_username:
                return fun(*args,**kwargs)
        return redirect("/login/")
    return inner

@csrf.exempt
@main.route("/register/",methods=["GET","POST"])
def register():
    result={"data":""}
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                result["data"]="用户存在"
            else:
                password = form_data.get("password")
                identify = form_data.get("identify")

                user = User()
                user.username = username
                user.password = password
                user.identify = identify
                user.save()
                return redirect("/login/")
    return render_template("register.html",**locals())

@csrf.exempt
@main.route("/login/",methods=["GET","POST"])
@main.route("//",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username and password:
            user = User.query.filter_by(username = username).first()
            if user:
                user_id = user.id
                response = redirect("/index/")
                response.set_cookie("username",username)
                response.set_cookie("user_id",str(user_id))
                response.set_cookie("user_identify",user.identify)
                session["username"] = username
                return response
    return render_template("login.html",**locals())


"""首页"""
@csrf.exempt
@main.route("/index/",methods=["GET","POST"])
@loginValid
# @cache.cached(timeout=2)
def index():
    user_id = request.cookies.get("user_id")
    user = User.query.filter_by(id = int(user_id)).first()
    response = make_response(render_template("index.html", **locals()))
    if not user.identify_id:   #身份信息不全
        if user.identify=="教师":
            return redirect("/complete_info1/")
        elif user.identify == "学生":
            return redirect("/complete_info2/")
    elif user.identify_id==1:  #教师
        response.set_cookie("identify_id","1")
        teacher = Teachers.query.filter_by(teacher_id=user.id).first()
        return redirect("/teacher_lists/")

    elif user.identify_id==2: #学生
        response.set_cookie("identify_id","2")
        return redirect("/student_lists/")

    else:  #其他人员
        return redirect("/register/")
    return response


@main.route("/logout/", methods=["GET", "POST"])
def logout():
    response = redirect("/login/")
    cookies=request.cookies
    for i in cookies:
        response.delete_cookie(i)
    return response

"""学生列表"""
@loginValid
@main.route("/student_lists/",methods=["GET","POST"])
def student_lists():
    user_lists = User.query.filter_by(identify="学生").all()
    return render_template("student_lists.html",**locals())
#路由带参数
@loginValid
@main.route("/student_list/<int:id>",methods=["GET","POST"])
def student_list(id):
    students = Students.query.filter_by().all()
    return render_template("student_lists.html",**locals())

"""教师列表"""
@loginValid
@main.route("/teacher_lists/",methods=["GET","POST"])
def teacher_lists():
    user_lists = User.query.filter_by(identify="教师").all()
    return render_template("student_lists.html", **locals())\


"""补全教师信息"""
@loginValid
@csrf.exempt
@main.route("/complete_info1/",methods=["GET","POST"])
def complete_info1():
    user_id = request.cookies.get("user_id")
    user = User.query.filter_by(id = int(user_id)).first()
    teacher_form = TeacherForm()
    courses = Course.query.all()
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("name")
        age = form_data.get("age")
        gender = form_data.get("gender")
        course = form_data.get("course")

        teacher = Teachers()
        teacher.username = username
        teacher.age = int(age)
        teacher.gender = gender
        teacher.course_id = int(course)
        teacher.teacher_id = user.id
        teacher.save()

        user.identify_id = 1
        user.save()
        return redirect("/teacher_lists/")
    return render_template("complete_info1.html", **locals())




"""补全学生信息"""
@loginValid
@csrf.exempt
@main.route("/complete_info2/", methods=["GET", "POST"])
def complete_info2():
    user_id = request.cookies.get("user_id")
    user = User.query.filter_by(id=int(user_id)).first()
    student_form = StudentForm()
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("name")
        age = form_data.get("age")
        gender = form_data.get("gender")

        student = Students()
        student.username = username
        student.age = int(age)
        student.gender = gender
        student.student_id = user.id
        student.save()

        user.identify_id = 2
        user.save()
        return redirect("/student_lists/")
    return render_template("complete_info2.html", **locals())

"""csrf错误页面"""
@csrf.error_handler
@main.route("/csrf_403/",methods=["GET","POST"])
def csrf_token_error(csrf_error):
    print(csrf_error)
    return render_template("csrf_403.html",**locals())


"""用户名ajax校验"""
@main.route("/usernameValid/",methods=["GET","POST"])
def usernameValid():

    result = {"code":"","data":""}
    # ajax前端校验get请求
    if request.method=="GET":
        username = request.args.get("username")
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                result["code"] = "400"
                result["data"] = "用户已存在"
            else:
                result["code"] = "200"
                result["data"] = "可以注册"
    # ajax前端校验post请求
    elif request.method == "POST":
        username = request.form.get("username")
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                result["code"] = "400"
                result["data"] = "用户已存在"
            else:
                result["code"] = "200"
                result["data"] = "可以注册"

    return jsonify(result)



"""模板页"""
@main.route("/base/",methods=["GET","POST"])
def base():
    return render_template("base.html",**locals())



# @main.route("/cache/",methods=["GET","POST"])
# @cache.cached(timeout=10)
# def cache_demo():
#     a=10
#     print(a)
#     return render_template("base.html")





