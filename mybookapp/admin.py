from mybookapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from mybookapp.models import Sach, LoaiSach, UserRole
from flask_login import current_user, logout_user, login_required
from flask_admin import BaseView, expose
from flask import redirect


# Tạo admin interface
admin = Admin(app=app, name="E-commerce Administration", template_mode="bootstrap4")


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class SachView(AuthenticatedModelView):
    # Hiển thị danh sách các trường trong admin
    column_list = ['tenSach', 'theLoai', 'soLuong', 'donGia','active', 'ngayTao','image' , 'loai.tenTheLoai']

    # Các trường được hiển thị trong form thêm/sửa
    form_columns = ['tenSach', 'theLoai', 'soLuong', 'donGia', 'active', 'image', 'maTheLoai']

    # Tùy chỉnh tên cột hiển thị
    column_labels = {
        'tenSach': 'Book Name',
        'theLoai': 'Category',
        'soLuong': 'Quantity',
        'donGia': 'Price',
        'active': 'Active',
        'image' : 'Image',
        'ngayTao' : 'NgayTao',
        'loai.tenTheLoai': 'Category Name',
        'maTheLoai': 'Category ID'
    }


class LoaiSachView(AuthenticatedModelView):
    # Hiển thị danh sách các trường trong admin
    column_list = ['tenTheLoai']

    # Các trường được hiển thị trong form thêm/sửa
    form_columns = ['tenTheLoai']

    # Tùy chỉnh tên cột hiển thị
    column_labels = {
        'tenTheLoai': 'Category Name'
    }

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(SachView(Sach, db.session))
admin.add_view(LoaiSachView(LoaiSach, db.session))
admin.add_view(LogoutView(name='Logout'))