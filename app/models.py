from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(511), unique=True)
    symptoms = db.relationship('Symptom', backref='disease', lazy='dynamic')

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(511))
    embedded_description = db.Column(db.String(511))
    disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'))

from app import db