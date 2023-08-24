from flask import Flask
# from app.app import app
# from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

from app import routes, models