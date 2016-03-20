# JWT Token auth
from vwauth.datastore import user_datastore
from flask.ext.security.utils import encrypt_password, verify_password
from flask_jwt import JWT
def authenticate(username, password):
    user = user_datastore.find_user(email=username)
    if user and username == user.email and verify_password(password, user.password):
        return user
    return None


def load_user(payload):
    user = user_datastore.find_user(id=payload['identity'])
    return user

jwt = JWT(app=None,authentication_handler=authenticate, identity_handler=load_user)
