# -*- coding: utf-8 -*-
"""User forms."""
from flask_security.forms import ConfirmRegisterForm, Required, TextField

class ExtendedRegisterForm(ConfirmRegisterForm):
    name = TextField('Name', [Required()])
    affiliation = TextField('Affiliation', [Required()])
    state = TextField('State', [Required()])
    city = TextField('City', [Required()])
