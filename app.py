from flask import Flask
from config import Configuration
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

from models import *

### admin ###
admin = Admin(app)
admin.add_view(ModelView(Post,db.session))
admin.add_view(ModelView(Tag,db.session))




