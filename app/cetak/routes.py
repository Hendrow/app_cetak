from flask import Blueprint, render_template, redirect, request, url_for, flash
from app import db
from app.models import Rekap, Cetak
from app.cetak.forms import FormCetak, FormEdit


mod = Blueprint('cetak',__name__,template_folder='templates')


@mod.route('/cetak')
def index():
    data = Cetak.query.order_by(Cetak.tanggal.desc()).all()
    return render_template('log_cetak.html', data = data, title='Catatan', page='Cetak per-petugas')


@mod.route('/cetak/input/<int:id>', methods=['GET','POST'])
def cetak(id):
    form = FormCetak()      
    if form.validate_on_submit():
        cetak = Cetak(jumlah=form.jumlah.data, petugas=form.petugas.data, tanggal=form.tanggal.data, no_rekap=id)
        db.session.add(cetak)
        db.session.commit()

        rekap = Rekap.query.filter_by(nomor=id).first() 
        petugas = form.petugas.data
        if petugas == 'agung':
            if rekap.agung =="-":
                agung = "0"
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.agung = int(form.jumlah.data) + int(agung)
            else:
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.agung = int(form.jumlah.data) + rekap.agung           
        elif petugas =='andi':
            if rekap.andi =="-":
                andi = "0"
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.andi = int(form.jumlah.data) + int(andi)
            else:
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.andi = int(form.jumlah.data) + rekap.andi
        elif petugas =='azizil':
            if rekap.azizil =="-":
                azizil = "0"
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.azizil = int(form.jumlah.data) + int(azizil)
            else:
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.azizil = int(form.jumlah.data) + rekap.azizil
        elif petugas =='ilham':
            if rekap.ilham =="-":
                ilham = "0"
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.ilham = int(form.jumlah.data) + int(ilham)
            else:
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.ilham = int(form.jumlah.data) + rekap.ilham
        elif petugas =='sandra':
            if rekap.sandra =="-":
                sandra = "0"
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.sandra = int(form.jumlah.data) + int(sandra)
            else:
                rekap.total = rekap.total + int(form.jumlah.data)
                rekap.sandra = int(form.jumlah.data) + rekap.sandra
         
        db.session.commit()
        flash('Pencatatan cetak laporan berhasil!','info')
        return redirect(url_for('cetak.index'))

    return render_template('cetak.html',form=form, title='Cetak Laporan', page='Catatan')


@mod.route('/cetak/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    pass
    form = FormEdit()
    c = Cetak.query.get_or_404(id)
    if form.validate_on_submit():       

        # cari selisih perubahan
        jml_awal = c.jumlah
        jml_ubah = int(form.jumlah.data)

        if jml_awal > jml_ubah:
            selisih = jml_awal - jml_ubah
            dikurangi=True
        elif jml_awal < jml_ubah:
            selisih = jml_ubah - jml_awal
            dikurangi=False

        r = Rekap.query.filter_by(nomor = c.no_rekap).first()
        if r:
            if c.petugas == 'agung':
                if dikurangi:
                    r.agung = r.agung - selisih
                    r.total = r.total - selisih
                else:
                    r.agung = r.agung + selisih
                    r.total = r.total + selisih
            if c.petugas == 'andi':
                if dikurangi:
                    r.andi = r.andi - selisih
                    r.total = r.total - selisih
                else:
                    r.andi = r.andi + selisih
                    r.total = r.total + selisih
            if c.petugas == 'azizil':
                if dikurangi:
                    r.azizil = r.azizil - selisih
                    r.total = r.total - selisih
                else:
                    r.azizil = r.azizil + selisih
                    r.total = r.total + selisih
            if c.petugas == 'ilham':
                if dikurangi:
                    r.ilham = r.ilham - selisih
                    r.total = r.total - selisih
                else:
                    r.ilham = r.ilham + selisih
                    r.total = r.total + selisih
            if c.petugas == 'sandra':
                if dikurangi:
                    r.sandra = r.sandra - selisih
                    r.total = r.total - selisih
                else:
                    r.sandra = r.sandra + selisih
                    r.total = r.total + selisih
            
            # update data di table rekap
            db.session.commit()

            # update data jumlah di table cetak
            c.jumlah = form.jumlah.data
            db.session.commit()
            flash('Data berhasil di update!','info')
            return redirect(url_for('cetak.index'))

    form.petugas.data = c.petugas
    form.jumlah.data = c.jumlah

    return render_template('edit_cetak.html', form=form, page='Edit', title='Edit')


@mod.route('/cetak/hapus/<int:id>', methods=['GET','POST'])
def hapus(id):
    cetak = Cetak.query.get_or_404(id)
    if cetak:
        rekap = Rekap.query.filter_by(nomor=cetak.no_rekap).first()
        if rekap:
            # cari petugas
            if cetak.petugas =='agung':
                rekap.agung = rekap.agung - cetak.jumlah
                rekap.total = rekap.total - cetak.jumlah
            elif cetak.petugas =='andi':
                rekap.andi = rekap.andi - cetak.jumlah
                rekap.total = rekap.total - cetak.jumlah
            elif cetak.petugas =='azizil':
                rekap.azizil = rekap.azizil - cetak.jumlah
                rekap.total = rekap.total - cetak.jumlah
            elif cetak.petugas =='ilham':
                rekap.ilham = rekap.ilham - cetak.jumlah
                rekap.total = rekap.total - cetak.jumlah
            elif cetak.petugas =='sandra':
                rekap.sandra = rekap.sandra - cetak.jumlah
                rekap.total = rekap.total - cetak.jumlah
            # update data pada table rekap
            db.session.commit()

            # menghapus data dalam table cetak
            db.session.delete(cetak)
            db.session.commit()
            flash('Data sudah dihapus!','info')
            return redirect(url_for('cetak.index'))