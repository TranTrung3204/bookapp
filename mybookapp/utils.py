from wtforms.validators import email

from mybookapp import app,db
from mybookapp.models import TaiKhoan
import hashlib

def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = TaiKhoan(name = name.strip(),
                    username = username.strip(),
                    password = password,
                    email = kwargs.get('email'),
                    avatar = kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()