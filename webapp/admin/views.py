from flask import Blueprint, flash, redirect, url_for, render_template
from webapp.user.models import User
from webapp.db import db
from flask_login import current_user, login_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/cabinet')
@login_required
def cabinet():
    if current_user.status == 'admin':
        all_inf = User.query.all()
        return render_template(
            'cabinet.html',
            all_inf=all_inf,
            )
    return 'Ты не админ, свяжись с админом!'


@blueprint.route('/cabinet')
def changed_status():
    
    
    
@blueprint.route('/del/<int:id>')
def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('user.cabinet'))
