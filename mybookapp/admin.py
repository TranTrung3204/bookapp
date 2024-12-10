from mybookapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from mybookapp.models import Sach, LoaiSach

# Tạo admin interface
admin = Admin(app=app, name="E-commerce Administration", template_mode="bootstrap4")


class SachView(ModelView):
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


class LoaiSachView(ModelView):
    # Hiển thị danh sách các trường trong admin
    column_list = ['tenTheLoai']

    # Các trường được hiển thị trong form thêm/sửa
    form_columns = ['tenTheLoai']

    # Tùy chỉnh tên cột hiển thị
    column_labels = {
        'tenTheLoai': 'Category Name'
    }


# Thêm các view vào Flask-Admin
admin.add_view(SachView(Sach, db.session))
admin.add_view(LoaiSachView(LoaiSach, db.session))

