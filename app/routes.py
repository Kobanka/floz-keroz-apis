from flask import Blueprint, request, jsonify
from . import db
from .models import User, Expense
from datetime import datetime

bp = Blueprint('api', __name__)

# Endpoint pour créer un utilisateur
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        password=data['password'],
        genre=data['genre'],
        revenu=data['revenu']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur créé avec succès'}), 201

# Endpoint pour créer une dépense
@bp.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    expense = Expense(
        user_id=data['user_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        description=data['description'],
        categorie=data['categorie'],
        montant=data['montant']
    )
    db.session.add(expense)
    db.session.commit()
    return jsonify({'message': 'Dépense ajoutée avec succès'}), 201

# Endpoint pour lister les utilisateurs
@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'nom': user.nom,
        'prenom': user.prenom,
        'email': user.email,
        'genre': user.genre,
        'revenu': user.revenu
    } for user in users]), 200

# Endpoint pour lister les dépenses d'un utilisateur
@bp.route('/expenses/<int:user_id>', methods=['GET'])
def get_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': expense.id,
        'date': expense.date.strftime('%Y-%m-%d'),
        'description': expense.description,
        'categorie': expense.categorie,
        'montant': expense.montant
    } for expense in expenses]), 200


# Endpoint pour afficher un seul utilisateur
@bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    return jsonify({
        'id': user.id,
        'nom': user.nom,
        'prenom': user.prenom,
        'email': user.email,
        'genre': user.genre,
        'revenu': user.revenu
    }), 200