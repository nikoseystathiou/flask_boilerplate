from application.public import public_bp
from flask import render_template

@public_bp.route('/')
@public_bp.route('/index')
def index():
    return render_template('public.html')