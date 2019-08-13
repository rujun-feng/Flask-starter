# coding: utf-8

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, model
from app.cmd.demo import Demo

app = create_app('Local') #Local|Dev|Prd

manager = Manager(app)
migrate = Migrate(app, model.db)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))
manager.add_command("demo", Demo())

if __name__ == '__main__':
	manager.run()