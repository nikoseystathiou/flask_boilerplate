from flask import Blueprint

public_bp = Blueprint('public', __name__,
                      template_folder='front')
from application.public.views import *
