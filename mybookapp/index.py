from flask import Flask, render_template, request, redirect, url_for
from mybookapp import app,login
import cloudinary.uploader
import utils
from flask_login import login_user, logout_user
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

        # Kiểm tra đăng nhập với vai trò ADMIN
        user = utils.check__login(username=username, password=password, role=UserRole.ADMIN)

    if user:
        login_user(user=user)
        # Chuyển hướng trực tiếp đến trang admin
        return redirect('index.html')
    else:
        # Nếu đăng nhập thất bại, có thể trả về trang login với thông báo lỗi
        return render_template("index.html",
                               err_msg='Đăng nhập admin không thành công')



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


@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)
