import os

# DEBUG = True


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR, "../FlaskDirtory/manage_sys.sqlite")
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True