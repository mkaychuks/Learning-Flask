from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '23d482aeed3777bb905174a9c5097b32' # setting our secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # part to our database
db = SQLAlchemy(app) # sqlalchemy instance
bcrypt = Bcrypt(app) # password hashing
login_manager = LoginManager(app) # Flask-Login 

from src import routes