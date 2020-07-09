from flask import Blueprint, render_template,redirect, url_for
from app.models import Terima
from .forms import InputForm

mod = Blueprint('terima',__name__)

@mod.route('/terima', methods=['GET','POST'])
def index():
    form = InputForm()
    data = Terima.query.all()

    if form.validate_on_submit():
        sarpelkes = form.sarpelkes.data
        nomorwo = form.nomorwo.data
        petugas = form.petugas.data
        jumlah = form.jumlah.data
        tanggal = form.tanggal.data

        dt = Terima(sarpelkes=sarpelkes, nomorwo=nomorwo, petugas=petugas,jumlah=jumlah,tanggal=tanggal)
        db.session.add(dt)
        db.session.commit()
        flash('Data berhasil disimpan','Primary')
        return redirect(url_for('terima.index'))

    return render_template('log_terima.html', data=data, page='Terima laporan', title='Terima laporan', form=form)


@mod.route('/terima/input', methods=['POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        sarpelkes = form.sarpelkes.data
        nomorwo = form.nomorwo.data
        petugas = form.petugas.data
        jumlah = form.jumlah.data
        tanggal = form.tanggal.data

        dt = Terima(sarpelkes=sarpelkes, nomorwo=nomorwo, petugas=petugas,jumlah=jumlah,tanggal=tanggal)
        db.session.add(dt)
        db.session.commit()
        flash('Data berhasil disimpan','Primary')
        return redirect(url_for('terima.index'))