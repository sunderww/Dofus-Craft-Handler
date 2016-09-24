from flask                          import *
from flask.ext.script               import Manager
from flask.ext.cors                 import CORS
from flask_principal                import *
from flask_migrate                  import Migrate, MigrateCommand
import flask.ext.login              as flask_login

from config                         import Config
from models.shared                  import db
from models.item.item               import Item
from models.item.recipe             import RecipeItem

# General Config
API_PREFIX = '/v1'

# App Config
app = Flask(__name__)
def config_app(verbose=False, debug=False):
    app.debug = debug
    Config(app, verbose=verbose, debug=debug)
    db.init_app(app)
    return app

# Plugins
CORS(app, supports_credentials=True)
principals = Principal(app)
migrate = Migrate(app, db)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
manager = Manager(config_app)
manager.add_command('db', MigrateCommand)
manager.add_option('-v', '--verbose', action='store_true', dest='verbose')
manager.add_option('-d', '--debug', action='store_true', dest='debug')


# Blueprints
from blueprints.item    import item_bp

api_blueprints = [
    item_bp,
]
for bp in api_blueprints: app.register_blueprint(bp, url_prefix=API_PREFIX)


# Manager methods
@manager.command
def load_database(filename):
    import json
    with open(filename) as json_file:
        items = json.load(json_file)
        for item_dct in items:
            item = Item.from_dict(item_dct)
            db.session.add(item)
        db.session.commit()

# Add useful classes to avoid importing everything each time you run a shell
@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Item=Item,
        RecipeItem=RecipeItem
    )

if __name__ == '__main__':
    manager.run()
