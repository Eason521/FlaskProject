from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template

from FlaskDirtory.main import app
from FlaskDirtory.main import csrf
from FlaskDirtory.main import session
from FlaskDirtory.forms import TeacherForm  #表单类使用

from FlaskDirtory.models import *




def loginvalid(fun):
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
@app.route("/register/",methods=["GET","POST"])
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
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username and password:
            user = User.query.filter_by(username = username).first()
            user_id = user.id
            print(user)
            response = redirect("/index/")
            response.set_cookie("username",username)
            response.set_cookie("user_id",str(user_id))
            session["username"] = username
            return response
    return render_template("login.html")


@csrf.exempt
@app.route("/index/",methods=["GET","POST"])
@loginvalid
def index():

    return render_template("index.html", **locals())

@app.route("/student_lists/",methods=["GET","POST"])
def student_lists():
    user_lists = User.query.filter_by(identify="学生").all()
    return render_template("student_lists.html",**locals())

@app.route("/teacher_lists/",methods=["GET","POST"])
def teacher_lists():
    user_lists = User.query.filter_by(identify="教师").all()
    return render_template("student_lists.html", **locals())\

@csrf.exempt
@app.route("/add_teacher/",methods=["GET","POST"])
def add_teacher():
    teacher_form = TeacherForm()
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("name")
        age = form_data.get("age")
        gender = form_data.get("gender")
        course = form_data.get("course")

        teacher = Teacher()
        teacher.username = username
        teacher.age = int(age)
        teacher.gender = gender
        teacher.course_id = int(course)
        teacher.save()
        return redirect("/teacher_lists/")
    return render_template("add_teacher.html", **locals())

@csrf.error_handler
@app.route("/csrf_403/",methods=["GET","POST"])
def csrf_token_error(csrf_error):
    print(csrf_error)
    return render_template("csrf_403.html",**locals())

@app.route("/usernameValid/",methods=["GET","POST"])
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











@app.route("/base/",methods=["GET","POST"])
def base():
    return render_template("base.html",**locals())







