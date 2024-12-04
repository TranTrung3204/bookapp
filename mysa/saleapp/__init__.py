from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/bookappdb?charset=utf8mB4'

db = SQLAlchemy(app=app)

