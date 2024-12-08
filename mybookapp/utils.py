import json, os

from wtforms.validators import email

from mybookapp import app,db
from mybookapp.models import TaiKhoan
import hashlib
# ham doc file json
def read_json(path):
    with open(path, "r") as f:
        return json. load(f)
#ham doc categories
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products():
    return read_json(os.path.join(app.root_path, 'data/products.json'))


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = TaiKhoan(name = name.strip(),
                    username = username.strip(),
                    password = password,
                    email = kwargs.get('email'),
                    avatar = kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()