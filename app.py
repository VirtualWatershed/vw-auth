import os

from flask import jsonify
from flask.ext.security import Security

from vwauth.settings import DevConfig, ProdConfig
from vwauth.app import create_app
from vwauth.database import db
from vwauth.user.forms import ExtendedRegisterForm


CONFIG = ProdConfig if os.environ.get('VWAUTH_ENV') == 'prod' else DevConfig

app = create_app(CONFIG)



@app.before_first_request
def create_db():
    db.create_all()
