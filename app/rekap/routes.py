from flask import Blueprint, render_template, redirect, request, url_for, flash
from app import db
from app.rekap.forms import FormInput, FormEdit, FormTanggal
from app.models import Rekap, Cetak


mod = Blueprint('rekap',__name__,template_folder='templates')

@mod.route('/')
@mod.route('/rekap')
def index():
    data = Rekap.query.order_by(Rekap.nomorwo.desc()).all()
    return render_template('beranda.html', title='Progress', page='Progress', data=data)

@mod.route('/rekap/input', methods=['GET','POST'])
def input():
    form = FormInput()

    if form.validate_on_submit():
        rekap = Rekap.query.filter_by(sarpelkes=form.sarpelkes.data).first()
        if rekap:
            if rekap.nomorwo == form.nomorwo.data:
                flash(f'Data {rekap.sarpelkes} dengan no.wo {rekap.nomorwo} sudah ada! ditahun {rekap.tahun}', 'danger')
                return redirect(url_for('rekap.index'))
            else:
                sarpelkes = form.sarpelkes.data
                nomorwo = form.nomorwo.data
                tahun = form.tahun.data
                agung = "-"
                andi = "-"
                azizil = "-"
                sandra = "-"
                ilham = "-"
                total= 0
                keterangan = "belum"

                # Simpan pada database
                data = Rekap(sarpelkes=sarpelkes, nomorwo=nomorwo, tahun=tahun, agung=agung, andi=andi, azizil=azizil, ilham=ilham, sandra=sandra, total=total, keterangan=keterangan)
                db.session.add(data)
                db.session.commit()
                flash('Data berhasil disimpan','success')
                return redirect(url_for('rekap.index'))
       
    return render_template('input_rekap.html', title='Tambah data', page='Tambah data', form=form)


@mod.route('/rekap/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    form = FormEdit()
    r = Rekap.query.get_or_404(id)
    if form.validate_on_submit():
        # simpan data ke table
        r.sarpelkes = form.sarpelkes.data
        r.nomorwo = form.nomorwo.data
        r.tahun = form.tahun.data
        r.keterangan = form.keterangan.data
        db.session.commit()
        flash('Data berhasil di update!','info')
        return redirect(url_for('rekap.index'))
    else:
        # Menampilkan data ke dalam FieldInput
        form.sarpelkes.data = r.sarpelkes
        form.nomorwo.data = r.nomorwo
        form.tahun.data = r.tahun
        form.keterangan.data= r.keterangan

        return render_template('edit_rekap.html', title='Edit Data', form=form)


@mod.route('/rekap/hapus/<int:id>', methods=['GET','POST'])
def hapus(id):
    r = Rekap.query.get(id)
    if r:
        db.session.delete(r)
        db.session.commit()
        flash('Data telah dihapus!','info')
        return redirect(url_for('rekap.index')) 


@mod.route('/rekap/kirim/<int:id>', methods=['GET','POST'])
def tanggal(id):
    r = Rekap.query.get_or_404(id)
    form = FormTanggal()
    if form.validate_on_submit():
        r.tgl_kirim = form.tgl_kirim.data
        db.session.commit()
        flash('Tanggal berhasil di update!','info')
        return redirect(url_for('rekap.index'))

    form.sarpelkes.data = r.sarpelkes
    form.nomorwo.data = r.nomorwo
    form.tgl_kirim.data = r.tgl_kirim
    return render_template('tgl_kirim.html', title='Edit Tanggal Kirim', form=form)
    


    