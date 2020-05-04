import os.path as op
from flask import url_for, redirect, request, abort
from flask_security import current_user
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'files')

class CustomView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/custom_index.html')

class UserModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

    column_list = ['email', 'first_name', 'last_name', 'roles']
    form_excluded_columns = ('password')

class RoleModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))