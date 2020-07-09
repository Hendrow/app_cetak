from flask import Blueprint, render_template

mod = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@mod.route('/login')
def login():
    return render_template('login.html')