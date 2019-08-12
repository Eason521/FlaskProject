from app import models,create_app
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

app = create_app("p ") #

manager = Manager(app)

migrate = Migrate(app,models)
manager.add_command("db",MigrateCommand)




if __name__ == '__main__':
    manager.run()