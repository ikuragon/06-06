from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_sqlalchemy import SQLAlchemy

from .db import db
from .config import Config

#from app.templates import bp


from .models import Employee, Position, Division, Job

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1029@localhost:5432/lb5_6"

db.init_app(app)
migrate = Migrate(app, db)




from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .views import views as views_blueprint
app.register_blueprint(views_blueprint)



login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#return app
