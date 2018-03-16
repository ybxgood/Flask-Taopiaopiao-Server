from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


model = SQLAlchemy()
migrate = Migrate()
loginManager= LoginManager()

def init_ext(app):
    model.init_app(app=app)
    migrate.init_app(app=app,db=model)
    loginManager.init_app(app)












