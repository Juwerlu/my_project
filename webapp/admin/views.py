from flask import Blueprint, flash, redirect, url_for, render_template
from webapp.user.models import User
from webapp.db import db
from flask_login import current_user, login_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/cabinet')
@login_required
def cabinet():
    if current_user.status == 'admin':
        return 'Привет, админ!'
    return 'Ты не админ, свяжись с админом!'
