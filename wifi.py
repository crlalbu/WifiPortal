from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
from dbwifi import DbWifi
import os

app = Flask(__name__)

DB = DbWifi()

@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Have Fun!!!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong Password!!!')
        return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)