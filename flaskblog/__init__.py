from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)   # __name__ is equal to __main__
# use Python to get the random bytes: import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'a0b645caee78ca9c9c5f920ca7980c67'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
