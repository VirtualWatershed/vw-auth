# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    # 'libs/bootstrap/dist/css/bootstrap.css',
    'css/site.css',
    'libs//bootswatch-dist/css/bootstrap.min.css',

    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/bootswatch-dist/js/bootstrap.min.js',
    'js/plugins.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
