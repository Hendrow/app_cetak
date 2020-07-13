from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    sarpelkes = StringField('Nama Sarpelkes', validators=[DataRequired()])
    nomorwo = StringField('Nomor wo', validators=[DataRequired()])
    petugas = SelectField(
        'Nama petugas',
        choices=[('none', '--pilih petugas--'),('agung', 'M. Agung'), ('andi', 'Andi Purba'), ('azizil', 'Azizil T Putra'), ('ilham', 'M Ilham'), ('sandra', 'Sandra Monika')]
    )
    jumlah = StringField('Jumlah Cetak', validators=[DataRequired()])
    tanggal = DateField('Tanggal', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditForm(FlaskForm):
    sarpelkes = StringField('Nama Sarpelkes', validators=[DataRequired()])
    nomorwo = StringField('Nomor wo', validators=[DataRequired()])
    petugas = SelectField(
        'Nama petugas',
        choices=[('none', '--pilih petugas--'),('agung', 'M. Agung'), ('andi', 'Andi Purba'), ('azizil', 'Azizil T Putra'), ('ilham', 'M Ilham'), ('sandra', 'Sandra Monika')]
    )
    jumlah = StringField('Jumlah Cetak', validators=[DataRequired()])
    tanggal = DateField('Tanggal', validators=[DataRequired()])
    submit = SubmitField('Update')


