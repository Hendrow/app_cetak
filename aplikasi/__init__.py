from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from aplikasi import models

from aplikasi.rekap.routes import mod
app.register_blueprint(rekap.routes.mod)

from aplikasi.catatan.routes import mod
app.register_blueprint(catatan.routes.mod)

from aplikasi.terima.routes import mod
app.register_blueprint(terima.routes.mod)

from aplikasi.auth.routes import mod
app.register_blueprint(auth.routes.mod)

