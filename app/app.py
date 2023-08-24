from flask import Flask
from flask_cors import CORS
# from app.app import app
# from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

from app import routes, models