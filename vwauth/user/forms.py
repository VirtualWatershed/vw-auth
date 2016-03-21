# -*- coding: utf-8 -*-
"""User forms."""
from flask_security.forms import RegisterForm, ConfirmRegisterForm, Required, TextField

class VWRegisterFormMixin(object):
    name = TextField('Name', [Required()])
    affiliation = TextField('Affiliation', [Required()])
    state = TextField('State', [Required()])
    city = TextField('City', [Required()])

class ExtendedConfirmRegisterForm(VWRegisterFormMixin, ConfirmRegisterForm):
    pass

class ExtendedRegisterForm(VWRegisterFormMixin, RegisterForm):
    pass
