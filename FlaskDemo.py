from flask import Flask

from flask import render_template

app=Flask(__name__)


@app.route('/')
def flaskdemo():
    return "我"

@app.route('/index/',methods=["GET","POST"])
def index():
    student_lists = [
        {"name":"张三","age":20,"phone":"13478272994"},
        {"name":"李四","age":14,"phone":"23423424322"},
        {"name":"王五","age":25,"phone":"23423453224"},
        {"name":"小六","age":26,"phone":"13353342442"},
        {"name":"阿七","age":17,"phone":"13344534538"},
    ]
    return render_template("index.html",student_lists=student_lists)

@app.route('/base/')
def base():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(debug=True)