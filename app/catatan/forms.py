from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class FormCetak(FlaskForm):
    jumlah = StringField('Jumlah Cetak', validators=[DataRequired()])
    petugas = SelectField(
        'Nama petugas',
        choices=[('None', '--Pilih petugas--'),('agung', 'M. Agung'), ('andi', 'Andi Purba'), ('azizil', 'Azizil T Putra'), ('ilham', 'M Ilham'), ('sandra', 'Sandra Monika')]
    )
    tanggal = DateField('Tanggal', validators=[DataRequired()])
    submit=SubmitField('Simpan')


class FormEdit(FlaskForm):
    petugas = StringField('Nama petugas', validators=[DataRequired()])
    jumlah = StringField('Jumlah cetak', validators=[DataRequired()])
    submit = SubmitField('Update')