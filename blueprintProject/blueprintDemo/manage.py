from flask import Flask

from blueprintDemo import blueprint1
from blueprintDemo import blueprint2

app = Flask(__name__)
app.register_blueprint(blueprint1.simple_blueprint1)  # 注册
app.register_blueprint(blueprint2.simple_blueprint2)  # 注册

if __name__ == '__main__':
    app.run()