from flask import Blueprint, render_template,redirect, url_for, flash
from app import db
from app.models import Terima
from .forms import InputForm, EditForm

mod = Blueprint('terima',__name__)

@mod.route('/terima')
def index():
    data = Terima.query.all()

    return render_template('log_terima.html', data=data, page='Terima laporan', title='Terima laporan')


@mod.route('/terima/input', methods=['GET','POST'])
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

    return render_template('input_terima.html', page='Input data', title='Terima laporan', form=form)


@mod.route('/terima/edit/<int:id>')
def edit(id):
    form = EditForm()
    t = Terima.query.get_or_404(id)
    if form.validate_on_submit():
        t.sarpelkes = form.sarpelkes.data
        t.nomorwo = form.nomorwo.data
        t.petugas = form.petugas.data
        t.jumlah = form.jumlah.data
        t.tanggal = form.tanggal.data
        db.session.commit()
        flash('Data berhasil di update!', 'Success')
        return redirect('terima.index')

    form.sarpelkes.data = t.sarpelkes
    form.nomorwo.data = t.nomorwo
    form.petugas.data = t.petugas
    form.jumlah.data = t.jumlah
    form.tanggal.data = t.tanggal

    return render_template('edit_terima.html', form=form, title='Terima laporan', page='Edit data')


@mod.route('/terima/edit/<int:id>')
def hapus(id):
    pass