import math
from flask import Flask, render_template, request, redirect, url_for
from mybookapp import app
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
        name = request.form.get('fullname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')

        try:
            if password.strip().__eq__(confirm.strip()):
              utils.add_user(name=name, username=username, password= password, email=email)
              return redirect('login')

            else:
                err_msg = 'Mat khau khong khop'
        except Exception as ex:
            err_msg = 'He thong loi: ' +str(ex)
    return render_template("register.html")


if __name__ == "__main__":

    app.run(debug=True)
