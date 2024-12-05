from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bookappdb?charset=utf8mB4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'jdsiuasgdigwofci8aegwaifdscij##$#@#!Édc'

db = SQLAlchemy(app=app)

