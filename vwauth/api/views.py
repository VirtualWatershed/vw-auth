# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from werkzeug.datastructures import MultiDict

from flask import Blueprint, flash, redirect, render_template, request, url_for, redirect, request, jsonify

from flask.ext.security import logout_user, login_required
from flask.ext.security import current_user
from flask_jwt import _default_jwt_encode_handler, jwt_required, current_identity


from vwauth.user.models import User
from vwauth.auth import jwt
from vwauth.extensions import security
from vwauth.datastore import user_datastore
from vwauth.constants import API_ENDPOINT

blueprint = Blueprint('api', __name__, static_folder='../static')

@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template('api/home.html')


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('api.home'))

@blueprint.route('{api}/apikey'.format(api=API_ENDPOINT), methods=['GET', 'POST'])
@login_required
def apikey():
    key = _default_jwt_encode_handler(current_user)
    return render_template('api/apikey.html',apikey=key)

@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user =  user_datastore.get_user(current_user.email)
    return render_template('api/profile.html',user=user)
