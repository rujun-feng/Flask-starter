# coding: utf-8

from werkzeug.security import check_password_hash
from .models import model
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	return model.User.get_by_domain([['id', '=', user_id]]).first()


def do_login(username, password):
	"""An simple login for demo"""

	user = model.User.get_by_domain([['username', '=', username]]).first()

	if user is None:
		return False

	is_pwd_ok = check_password_hash(user.password, password)
	return user if is_pwd_ok else False