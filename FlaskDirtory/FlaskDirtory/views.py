from flask import redirect
from flask import render_template
from flask import request

from FlaskDirtory.main import app
from FlaskDirtory.models import *



@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        identify = form_data.get("identify")

        user = User()
        user.username = username
        user.password = password
        user.identify = identify
        user.save()
        return redirect("/login/")
    return render_template("register.html")

@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username and password:
            response = redirect("/index/")
            response.set_cookie("username",username)

            return response
    return render_template("login.html")


@app.route("/index/",methods=["GET","POST"])
def index():

    return render_template("index.html", **locals())

@app.route("/student_lists/",methods=["GET","POST"])
def student_lists():
    user_lists = User.query.all()

    return render_template("student_lists.html",**locals())



@app.route("/base/",methods=["GET","POST"])
def base():
    return render_template("base.html",**locals())







