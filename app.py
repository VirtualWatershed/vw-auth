import os
from vwauth.settings import DevConfig, ProdConfig
from vwauth.app import create_app
from vwauth.database import db
from flask.ext.security import Security
#from vwauth.user.models import user_datastore
from vwauth.user.forms import ExtendedRegisterForm

# Security
#from flask.ext.security import SQLAlchemyUserDatastore
#from vwauth.datastore import user_datastore
#from vwauth.user.models import User, Role
#from flask_jwt import jwt_required, current_identity
from flask import jsonify

CONFIG = ProdConfig if os.environ.get('VWAUTH_ENV') == 'prod' else DevConfig

app = create_app(CONFIG)
#user_datastore = SQLAlchemyUserDatastore(db,User,Role)
#security = Security(app,datastore=user_datastore,confirm_register_form=ExtendedRegisterForm)



@app.before_first_request
def create_db():
    db.create_all()

# @app.route('/api/v1/test',methods=['GET'])
# @jwt_required()
# def test_jwt():
#     return jsonify({"description":"Passed!","data":current_identity.name})
