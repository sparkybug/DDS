# from flask.cli import FlaskGroup
# from app import app, db

# cli = FlaskGroup(app)

# if __name__ == '__main__':
#     cli()

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)

# adding the migrateCommand to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()