from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin
import cloudinary


app = Flask("__name__")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/bookappdb?charset=utf8mb4" % quote ('@Admin123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'jdsiuasgdigwofci8aegwaifdscij##$#@#!Édc'

cloudinary.config(
    cloud_name = 'djbi959vf',
    api_key =  '773466584879955',
    api_secret =  'N-dr2IIPhCScs9UXgtsPNoDE9_g',
)

db = SQLAlchemy(app=app)

