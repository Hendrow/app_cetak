from flask import Blueprint

mod = Blueprint('terima',__name__)

@mod.route('/terima')
def index():
    return "hello terima page!"