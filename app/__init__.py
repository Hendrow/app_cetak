from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app.rekap.routes import mod
from app.catatan.routes import mod
from app.terima.routes import mod
from app.auth.routes import mod


app.register_blueprint(rekap.routes.mod)
app.register_blueprint(catatan.routes.mod)
app.register_blueprint(terima.routes.mod)
app.register_blueprint(auth.routes.mod)