from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class FormInput(FlaskForm):
    sarpelkes = StringField('Sarpelkes', validators=[DataRequired()])
    nomorwo = StringField('No.WO', validators=[DataRequired()])
    tahun = StringField('Tahun', validators=[DataRequired()])
    submit = SubmitField('Simpan')


class FormEdit(FlaskForm):
    sarpelkes = StringField('Sarpelkes', validators=[DataRequired()])
    nomorwo = StringField('No.WO', validators=[DataRequired()])
    tahun = StringField('Tahun', validators=[DataRequired()])
    # agung = StringField('Lap. Agung', validators=[DataRequired()])
    # andi = StringField('Lap.Andi', validators=[DataRequired()])
    # azizil = StringField('Lap. Azizil', validators=[DataRequired()])
    # ilham = StringField('Lap. Ilham', validators=[DataRequired()])
    # sandra = StringField('Lap. Sandra', validators=[DataRequired()])
    # total = StringField('Total', validators=[DataRequired()])
    keterangan = StringField('Keterangan', validators=[DataRequired()])
    submit = SubmitField('Update')


class FormTanggal(FlaskForm):
    sarpelkes = StringField('Sarpelkes', validators=[DataRequired()])
    nomorwo = StringField('No.WO', validators=[DataRequired()])
    tgl_kirim = DateField('Tanggal Kirim', validators=[DataRequired()])
    submit = SubmitField('Update')



