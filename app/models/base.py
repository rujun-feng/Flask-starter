# coding: utf-8

import datetime
from flask_sqlalchemy import SQLAlchemy
#from app import db

db = SQLAlchemy()

class BaseModel(db.Model):

	__abstract__ = True

	@classmethod
	def _get_expression(cls, exp):
		field = exp[0]
		operater = exp[1]
		val = exp[2]
		field = getattr(cls, field)

		if operater == '=':
			return (field == val)
		if operater == 'is':
			return (field.is_(val))
		if operater == '!=':
			return (field != val)
		if operater == '>':
			return (field > val)
		if operater == '<':
			return (field < val)
		if operater == 'in':
			return (field.in_(val))
		if operater == 'not in':
			return (field.notin_(val))
		if operater == '>=':
			return (field >= val)
		if operater == '<=':
			return (field <= val)
		if operater == 'contains':
			return (field.contains(val))
		if operater == 'endwith':
			return (field.endswith(val))
		if operater == 'startwith':
			return (field.startswith(val))
		if operater == 'not like':
			return (field.notlike(val))
		if operater == 'like':
			return (field.like(val))

	@classmethod
	def get_all(cls):
		return cls.get_by_domain([]).all()

	@classmethod
	def get_by_domain(cls, domain):
		"""
			Query data by a domain which is a two-dimensional array.
			e.g:
				User.get_by_domain([['username', '=', 'demo']]).all()
				The example query the user table and condition is 'where name = demo',
			operater support:
				=,is,!=,>,<,in,not in,>=,<=,contains,endwith,startwith,not like,like
			Multiple-conditions e.g：
					where username = 'demo' and password = 'password'
						User.get_by_domain([['username', '=', 'demo'], ['password', '=', 'password']]).all()
					where username = 'demo' or password = 'password'
						User.get_by_domain(['|', ['username', '=', 'demo'], ['password', '=', 'password']]).all()
			the default condition is AND-condition:
				 [['username', '=', 'demo'], ['password', '=', 'password']] equals to
				 [
					'&', ['username', '=', 'demo'], ['password', '=', 'password']
				 ]
			OR-condition must be explicited:
				 [
					'|', ['username', '=', 'demo'], ['password', '=', 'password']
				 ]
			If the multiple-condition is very complex,the AND-OR condition must be explicited:
				User.get_by_domain([
					'|',
						'&', ['username', '=', 'de'], ['password', '=', 'password'],
						'&', ['email', 'like' ,'qq.com'], ['email', 'contains', 'abc']
				]).all()
				which means where (username = 'de' and password = 'password') or (email like 'qq.com' and email contains 'abc')
			But, i highly recommended that the complexible condition use get_by_sql function.
		"""
		def combine(left, andor, right):
			left = cls._get_expression(left)
			if isinstance(right, list):
				right = cls._get_expression(right)
			if andor == '&':
				return left & right
			if andor == '|':
				return left | right

		expression, left, right = None, None, None

		if '|' not in domain and '&' not in domain:

			for exp in domain:
				_expression = cls._get_expression(exp)
				if expression is None:
					expression = _expression
				else:
					expression = expression & _expression

		else:

			while len(domain) > 0:
				p = domain.pop()
				if p in ('|', '&'):
					right = combine(left, p, right)
					left = None
					continue

				if right is None:
					right = p
					continue

				if left is None:
					left = p

			expression = right

		if expression is not None:
			reads = cls.query.filter(expression)
		else:
			reads = cls.query
		return reads

	@classmethod
	def get_by_sql(cls, sql):
		'''query by sql'''
		items = db.session.execute(sql)
		return items

	@classmethod
	def create(cls, **args):
		self = cls(**args)
		db.session.add(self)
		db.session.flush()
		return self
	
	def update(self, **args):
		for key in args:
			if key != 'id':
				setattr(self, key, args[key])
		db.session.flush()
		return True

	@classmethod
	def remove(cls, item):

		if isinstnace(item, int):
			model_ = cls.get_by_domain([['id', '=', item]]).first()
		else:
			model_ = item

		if issubclass(model_, BaseModel):
			db.session.delete(self)
			db.session.flush()
			return True

		return False

	@classmethod
	def commit(cls):
		db.session.commit()