import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BASE_CONFIG():
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "manage_sys.sqlite")
    # SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost/school"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "Tanyxn"  #用来生成sessionid 和csrf_token 必须加的配置

class DEBUG_CONFIG(BASE_CONFIG):
    DEBUG = True

class ONLINE_CONFIG(BASE_CONFIG):
    DEBUG = False