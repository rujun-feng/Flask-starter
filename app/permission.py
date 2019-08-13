# coding: utf-8

from flask import jsonify
from functools import wraps
from flask_login import current_user
from .models import model

def gen401resp():
	resp = jsonify({'code':401,'msg':'Sorry,you do not have the permission!'})
	resp.status_code = 401
	return resp

def check_permission(need_permissions=[]):
	"""check permission decorater"""

	def decorated_fn(fn):

		@wraps(fn)
		def decorated__fn(*args, **kwargs):
			user_permissions = permission.get_user_permissions(current_user)
			u_permissions = [up.name for up in user_permissions]
			is_permission_ok = len(list(set(u_permissions).intersection(set(need_permissions)))) > 0

			if not is_permission_ok:
				return gen401resp()
			else:
				return fn(*args, **kwargs)

		return decorated__fn

	return decorated_fn

def toUserModel(user):
	if isinstance(user, int):
		user = model.User.get_by_domain([['id', '=', user]]).first()
	elif isinstance(user, str):
		user = model.User.get_by_domain([['username', '=', user]]).first()
	return user

class Permission(object):

	def get_user_permissions(self, user):
		user = toUserModel(user)
		return user.permissions

	def create_permission(self, permission_name):
		new_permission = model.Permission.create(**{
			'name':permission_name
		})
		return new_permission

	def bind_permission(self, user, permissions):
		user = toUserModel(user)
		user.permissions = permissions
		return True

	def remove_permission(self, permission_id):
		p = model.Permission.get_by_domain([['id', '=', permission_id]]).first()

		### Clear the user related with this permission
		for u in p.users:
			model.User.remove(u)

		### Then remove the permision
		model.Permission.remove(p)

permission = Permission()