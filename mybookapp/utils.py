import json, os
from mybookapp import app
# ham doc file json
def read_json(path):
    with open(path, "r") as f:
        return json. load(f)
#ham doc categories
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products():
    return read_json(os.path.join(app.root_path, 'data/products.json'))
