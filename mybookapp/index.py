from flask import Flask, render_template, request, redirect, url_for, flash
from mybookapp import app,login
import cloudinary.uploader
import utils
from flask_login import login_user, logout_user, login_required
from mybookapp.models import UserRole


app = Flask(__name__)
from mybookapp.admin import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['get', 'post'])
def user_login():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check__login(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('index'))
        else:
            err_msg = 'Username hoặc password không chính xác!!'
    return render_template("login.html", err_msg=err_msg)


@app.route('/admin-login', methods=['post'])
def admin_login():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check__login(username=username, password=password, role=UserRole.ADMIN)

    if user:
        login_user(user=user)
        return redirect('/admin')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_login'))


@app.route("/register",methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        avatar_path = None
        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url']
                utils.add_user(name=name, username=username, password= password, email=email, avatar=avatar_path)
                return redirect('login')

            else:
                err_msg = 'Mat khau khong khop'
        except Exception as ex:
            err_msg = 'He thong loi: ' +str(ex)
    return render_template("register.html")


@app.route('/admin/book-import', methods=['GET', 'POST'])
@login_required
def admin_book_import():
    if request.method == 'POST':
        ten_sach = request.form['ten_sach']
        the_loai = request.form['the_loai']
        tac_gia = request.form['tac_gia']
        so_luong = int(request.form['so_luong'])

        # Kiểm tra số lượng sách nhập
        if so_luong < 150:
            flash('Số lượng sách nhập tối thiểu là 150.', 'danger')
            return redirect(url_for('admin_book_import'))

        # Kiểm tra số lượng sách tồn kho
        existing_book = Sach.query.filter_by(tenSach=ten_sach).first()
        if existing_book and existing_book.soLuong + so_luong > 300:
            flash(f'Số lượng tồn kho của sách "{ten_sach}" vượt quá 300.', 'danger')
            return redirect(url_for('admin_book_import'))

        # Lưu thông tin sách vào cơ sở dữ liệu
        new_book = Sach(
            tenSach=ten_sach,
            theLoai=the_loai,
            soLuong=so_luong,
            donGia=0,  # Thêm giá bán sau
            maTheLoai=1,  # Thêm mã thể loại sau
            loai=None  # Thêm liên kết với bảng LoaiSach sau
        )
        db.session.add(new_book)
        db.session.commit()

        flash('Nhập sách thành công.', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/book_import.html')

@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)
