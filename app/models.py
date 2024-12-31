from . import db
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(1), nullable=False)


    incomes = db.relationship('Income', backref='user', cascade="all, delete", lazy=True)
    expenses = db.relationship('Expense', backref='user', cascade="all, delete", lazy=True)

class Expense(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False) 
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    montant = db.Column(db.Float, nullable=False)

class Income(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    montant = db.Column(db.Float, nullable=False)