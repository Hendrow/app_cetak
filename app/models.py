from datetime import datetime
from app import db

class Rekap(db.Model):
    nomor = db.Column(db.Integer, primary_key=True)
    sarpelkes = db.Column(db.String(55), nullable=False)
    nomorwo = db.Column(db.String(8), nullable=False)
    tahun = db.Column(db.Integer)
    agung = db.Column(db.Integer)
    andi = db.Column(db.Integer)
    azizil = db.Column(db.Integer)
    ilham = db.Column(db.Integer)
    sandra = db.Column(db.Integer)
    total = db.Column(db.Integer)
    keterangan = db.Column(db.String(55))
    tgl_kirim = db.Column(db.DateTime)
    cetak = db.relationship('Cetak', backref='rekap', lazy='dynamic')

    def __repr__(self):
        return '<Sarpelkes {}>'.format(self.sarpelkes)

class Cetak(db.Model):
    nomor = db.Column(db.Integer, primary_key=True)
    jumlah = db.Column(db.Integer)
    petugas = db.Column(db.String(21), nullable=False)
    tanggal = db.Column(db.DateTime)
    no_rekap = db.Column(db.Integer, db.ForeignKey('rekap.nomor'))

    def __repr__(self):
        return '<petugas {}>'.format(self.petugas)

class Terima(db.Model):
    nomor = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    jumlah = db.Column(db.Integer)
    sarpelkes = db.Column(db.String(55), nullable=False)
    nomorwo = db.Column(db.String(8), nullable=False)
    petugas = db.Column(db.String(25))

    def __repr__(self):
        return '<Sarpelkes {}>'.format(self.sarpelkes)
