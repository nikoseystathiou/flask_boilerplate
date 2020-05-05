from flask import Flask, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_security import Security, SQLAlchemyUserDatastore
from flask_babelex import Babel
from flask_admin import Admin, helpers as admin_helpers
from application.models import db
from application.public import public_bp
from application.models.models import *
from application.admin.views import *
from flask_migrate import Migrate

def create_app(config_filename, debug):
    # Instantiate the Flask application with configurations
    app = Flask(__name__, instance_relative_config=True)
    app.debug = debug
    # Instantiate Configs
    app.config.from_object(config_filename)

    path = op.join(op.dirname(__file__), 'static')
    # Instantiate the debug toolbar. Only for debug true
    toolbar = DebugToolbarExtension(app)

    # Initialize babel
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        if request.args.get('lang'):
            session['lang'] = request.args.get('lang')
        return session.get('lang', 'en')

    db.init_app(app)
    # Init Migrations
    migrate = Migrate(app, db)

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    register_blueprints(app)

    # Create admin
    admin = Admin(
        app,
        'My Dashboard',
        base_template='my_master.html',
        template_mode='bootstrap3',
    )

    # Add model views
    admin.add_view(UserModelView(User, db.session, name='Users'))
    admin.add_view(RoleModelView(Role, db.session, name="Roles"))
    admin.add_view(CustomView(name="Custom view", endpoint='custom'))
    
    # define a context processor for merging flask-admin's template context into the
    # flask-security views.
    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )

    return app

def register_blueprints(app):
    app.register_blueprint(public_bp, url_prefix='/')
