from flask import Flask
# from app.app import app
# from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import routes, models