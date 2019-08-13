from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import transaction, model
from app.permission import check_permission

demo = Blueprint('demo', __name__)

@demo.route('/')
@login_required
def index():
	uname = current_user.username
	articles = [{
		'title':a.title,
		'content':a.content
	}for a in current_user.articles]
	return jsonify({'code':200, 
					'messge':'Hello {0}, welcome to flask-starter!'.format(uname),
					'your articles':articles})

@demo.route('/admin')
@check_permission(['admin'])
@login_required
def aidmin_ndex():
	uname = current_user.username
	return jsonify({'code':200, 'messge':'Hello {0}, You are the administrator!'.format(uname) })

@demo.route('/article', methods=['POST'])
@transaction
@login_required
def create_article():
	title = request.form.get('title')
	content = request.form.get('content')
	model.Article.create(**{
		'title':title,
		'content':content
	})
	return jsonify({'code':200, 'messge':'Create article Successfully!'})