from app.app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b3223848c57ce9:bdbf90ed@us-cdbr-east-06.cleardb.net/heroku_db25d753792fa31'

db = SQLAlchemy(app)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(511), unique=True)
    symptoms = db.relationship(
        'Symptom', backref='disease', lazy='dynamic')

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(511))
    embedded_description = db.Column(db.String(65211))
    disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'))