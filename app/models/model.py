# coding: utf-8

from .base import BaseModel, db
from flask_login import UserMixin

__all__ = ['db', 'User', 'Permission']

def init_app(app):
	db.init_app(app)

### User and Permission related table ###
upermissions = db.Table('upermissions',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)

class User(BaseModel, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(128))
	permissions = db.relationship('Permission', secondary=upermissions,
	 lazy='dynamic', backref=db.backref('users', lazy=True))


class Permission(BaseModel):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))


class Article(BaseModel):
	'''demo article model'''
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), nullable=False)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('articles', lazy='dynamic'))