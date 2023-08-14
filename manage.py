# from flask.cli import FlaskGroup
# from app import app, db

# cli = FlaskGroup(app)

# if __name__ == '__main__':
#     cli()

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app, create_app,  db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

# adding the migrateCommand to the manager
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))

if __name__ == '__main__':
    manager.run()