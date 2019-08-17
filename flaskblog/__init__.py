from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)   # __name__ is equal to __main__
# use Python to get the random bytes: import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'a0b645caee78ca9c9c5f920ca7980c67'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
