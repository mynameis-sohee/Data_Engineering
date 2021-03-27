# 로그인 구현 기본 과정

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session #session : 로그인 구현에 필수적인 딕셔너리. url 통한 계정해킹 위험 감소 

ID ='d'
PW='d'

app=Flask(__name__)
app.secret_key = "dddvwedwdf"

@app.route('/')
def home():
    if 'userID' in session:
        return render_template("home.html",username = session.get("userId"), login=True)
    else:
        return render_template("home.html",login=False)

    pass



@app.route('/login', methods=['get'])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and _password_ == PW:
        session['userID'] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.pop("userId")
    redirect(url_for("home"))
    pass


if __name__=='__main__':
    app.run(port=5000, debug=False)
