import json
from flask import (
	Blueprint, 
	jsonify, 
	render_template, 
	request, 
	redirect,
	url_for
)
from flask_login import login_user, logout_user, login_required
from app.auth import do_login as _do_login

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return render_template('auth/login.html')

@auth.route('/do_login', methods=['POST'])
def do_login():
	username = request.form.get('user')
	password = request.form.get('password')
	user = _do_login(username, password)

	if user:
		login_user(user, False)
		return redirect('/')
	else:
		return render_template('auth/login.html', msg=u'The username or password is not correct!')

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect('/login')