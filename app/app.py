from flask import Flask
# from app.app import app
# from config import Config
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)

@api.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    api.run(debug=True)

from app import routes, models