from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask("__name__")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/bookappdb?charset=utf8mb4" % quote ('@Admin123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'jdsiuasgdigwofci8aegwaifdscij##$#@#!Édc'

db = SQLAlchemy(app=app)

