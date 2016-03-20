from flask.ext.security import SQLAlchemyUserDatastore
from vwauth.user.models import User, Role
from .extensions import db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
