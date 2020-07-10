from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '23d482aeed3777bb905174a9c5097b32' # setting our secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # part to our database
db = SQLAlchemy(app) # sqlalchemy instance


from src import routes