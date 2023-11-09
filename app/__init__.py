from flask import Flask
from flask_migrate import Migrate
from .database import db
from models.user import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)
migrate = Migrate(app, db)

from app import routes
