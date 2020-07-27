from flask import Blueprint, render_template, session, redirect, url_for, flash
from .forms import LoginForm

mod = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@mod.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "hendro" and form.password.data =="adminadmin09":
            session['username']= form.username.data
            return redirect(url_for('rekap.index'))
        else:
            flash('Username atau password anda salah!','danger')
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@mod.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('rekap.index'))