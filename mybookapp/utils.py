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

def check__login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                                     TaiKhoan.password.__eq__(password)).first()
def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)