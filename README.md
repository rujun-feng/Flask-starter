## 欢迎使用Flask-starter
[![pyversions](https://img.shields.io/badge/python-2.7-blue.svg)]()
[![ver](https://img.shields.io/badge/release-v1.0.0-green.svg)]()
[![MIT](https://img.shields.io/badge/license-MIT-purse.svg)]()

**Flask-starter** 的出现是为了让开发者能够更快速，更方便的使用flask框架，免去中间对很多常用flask的组件及第三方库的学习成本，从而能更快速更直接关注自己的业务逻辑。因为我发现flask的新手通常在开始一个项目前，除了去看flask官网的文档，还得研究如何连接数据库，处理api路由，生产环境如何跑起来的问题，这些问题的学习成本并不算小，Flask-starter就是为了解决这些问题而存在的。

## 适用人员
本项目适用于Flask初学者，或者需要适用python来迅速开发web程序的开发人员，本项目主要关注的还是web的后端逻辑，因为现在都是前后端分离，所以flask自带的jinja2模板引擎也已经很少使用。项目中的用到的模板引擎也只是为了达到demo的目的。

## 包含的功能
* 完整的代码框架
* 常见flask组件的集成
* 简单登录模块的实现
* 权限模块的实现
* 接口路由拆分
* 关系型数据库orm的拓展，实现model的增删改查等功能(CRUD)
* 与wsgi集成，可直接上生产环境运行

## 如何安装
此项目运行在linux或mac系统中, 从github上拉代码到本地：

	$ git clone https://github.com/rujun-feng/Flask-starter.git

安装virtualenv:

	$ pip install virtualenv

安装虚拟环境及关联的包:

	$ make env

修改config.py文件里的LocalConfig类中的数据库连接字符串SQLALCHEMY\_DATABASE\_URI，指向自己的关系型数据库(mysql,sqlite,postgresql等)，我的数据库连接字符串如下，**请自行更改**:

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flaskstarter?charset=utf8'

同步数据库及表结构:

	$ make initdb

插入demo数据(插入demo的用户及权限数据):

	$ make demo

执行启动:

	$ make run

若在生产环境启动，会使用gunicorn来启动，使用如下命令:

	$ make rung

在浏览器中输入 **localhost:5000**，管理员用户名/密码是**admin/123456**，即可访问.

访问**localhost:5000/logout**, 即可登出该账户

访问admin页面 **localhost:5000/admin**, 如果用user/123456的账号去访问，则返回无权限，因为demo数据中就只有admin账户是管理员权限.

## 常见问题

### 上生产时如何指定运行环境？
将manage.py文件中的Local改成Prd,并在config.py文件里配置ProductionConfig类的环境变量即可，
不同环境对应不同的环境变量，可自行添加和更改。

### 如何增加新的model？
在app/models/model.py文件中，新增自己的Model类，并继承**BaseModel**，这样你的Model就直接拥有了增删改查的方法了，项目中常见的字段定义已经给出，其他不太常用的类型的字段定义请参考官方文档[Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com "Title")

增加好model及字段后，使用命令来同步数据库表结构即可：

	$ make syncdb

### 如何新增接口?
在app/views/文件夹中新增自己的view文件，文件里需实例化Blueprint蓝本的对象，接着在app/__init__.py中在create_app里把你的接口路由注册进flask的app里，在本项目里，都可参考其他接口的实现方式。

### 如何在接口中判断当前用户是否有权限？
假设有个页面或接口是只有管理员才能访问的（假设管理员权限在权限表里的name为admin），则在你的view文件中的某个接口的定义中，添加**permission权限模块中的@check_permission**这个装饰器即可,详情请参考app/views/demo.py文件。

### model如何增删改查？
只要继承了**BaseModel**的model都拥有增删改查的功能，具体的代码请参考**app/cmd/demo.py或app/permission.py**中的实现方式。

### 为何在接口里面做了任何更改数据的操作，没有报错数据也没有改变？
在views文件夹下的非只读的接口，需要加上**装饰器@transaction**来保证每一次的更新数据的请求都是原子性的，所谓的原子性就是指一个事务的多条SQL语句，要么全部执行成功，要么就都没执行。数据没有改变的原因是数据库等待着事务的commit提交的操作，总之，加上这个装饰器就没问题了。


## 欢迎技术交流

我是冯汝俊,一名在杭州拼搏的工程师,如在使用过程中有任何问题请联系我~~

email:rujun15618458610@sina.com

qq:125997125

我会在空闲时间里回复的喔~~

