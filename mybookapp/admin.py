from mybookapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import render_template
from mybookapp.models import Sach, LoaiSach, NguoiDung



admin = Admin(app=app,
              name='Book Store Management',
              template_mode='bootstrap4',
              )

admin.add_view(ModelView(Sach, db.session))
admin.add_view(ModelView(LoaiSach, db.session))