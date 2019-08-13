# coding: utf-8
from werkzeug.security import generate_password_hash
from flask_script import Command
from app.models import model
from app.permission import permission

class Demo(Command):
    '''demo data'''

    def run(self):
        ###Insert admin user###
        new_user = model.User.create(**{
            'username':'admin',
            'password':generate_password_hash('123456')
        })

        ###Insert admin permission###
        new_permission = permission.create_permission('admin')

        ###bind permission###
        permission.bind_permission(new_user, [new_permission])

        ###Insert user
        new_user2 = model.User.create(**{
            'username':'user',
            'password':generate_password_hash('123456')
        })

        ###Insert admin article###
        new_article = model.Article.create(**{
            'title':'Curry',
            'content':'Curry (plural curries) is a variety of dishes originating in the Indian subcontinent',
            'user_id':new_user.id
        })

        new_article = model.Article.create(**{
            'title':'China',
            'content':"China, officially the People's Republic of China (PRC), is a country in East Asia and the world's most populous country",
            'user_id':new_user.id
        })

        ###Do not use commit function in your views,use transaction decorator###
        model.db.session.commit()