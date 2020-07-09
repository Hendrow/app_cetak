from flask import Blueprint, render_template
from app.models import Terima
from .forms import InputForm

mod = Blueprint('terima',__name__)

@mod.route('/terima')
def index():
    form = InputForm()
    data = Terima.query.all()

    if form.validate_on_submit():
        pass
    return render_template('log_terima.html', data=data, page='Terima laporan', title='Terima laporan', form=form)


@mod.route('/terima/input')
def input():
    pass
