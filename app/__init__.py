# coding: utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import config
from .models import model

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(env):
	app = Flask(__name__)
	app.config.from_object(config[env])

	model.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)

	### routers ###
	from .views.demo import demo as demo_bp
	app.register_blueprint(demo_bp)

	from .views.auth import auth as auth_bp
	app.register_blueprint(auth_bp)
	### routers end ###

	return app