import math
from flask import Flask, render_template, request, redirect, url_for
from mybookapp import app
import cloudinary.uploader
import utils

app = Flask(__name__)
from mybookapp.admin import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

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


if __name__ == "__main__":
    app.run(debug=True)
