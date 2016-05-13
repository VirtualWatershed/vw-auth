# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template

from vwauth import api
from vwauth.assets import assets
from vwauth.extensions import bcrypt, cache, csrf_protect, db, debug_toolbar, login_manager, migrate, mail, security, session
from vwauth.auth import jwt
from vwauth.settings import ProdConfig
from vwauth.datastore import user_datastore
from vwauth.user.forms import ExtendedRegisterForm, ExtendedConfirmRegisterForm


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)

    csrf_protect.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    session.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    security.init_app(app, datastore=user_datastore,
                      confirm_register_form=ExtendedConfirmRegisterForm, register_form=ExtendedRegisterForm)

    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(api.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
