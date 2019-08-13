# coding: utf-8

from functools import wraps
from flask import Response, jsonify
from .model import *

def transaction(fn):
	'''transaction decorator'''

	@wraps(fn)
	def decorated_function(*args, **kwargs):

		try:
			res = fn(*args, **kwargs)
			db.session.commit()
			return res

		except Exception, e:
			db.session.rollback()
			res = jsonify({'code':500,'msg':str(e)})
			res.status_code = 500
			return res

	return decorated_function