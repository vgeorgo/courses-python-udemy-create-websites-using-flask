import os
from flask import Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#### SQL DATABASE SECTION
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
########################

###### BLUEPRINT SECTION
from puppycompanyblog.core.views import core
app.register_blueprint(core)

from puppycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from puppycompanyblog.users.views import users
app.register_blueprint(users)
########################

########## LOGIN SECTION
from flask_login import LoginManager

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'
########################
