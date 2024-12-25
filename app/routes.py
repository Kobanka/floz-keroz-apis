from flask import Blueprint, request, jsonify
from . import db
from .models import User, Expense, Income
from datetime import datetime

bp = Blueprint('api', __name__)

# --- UTILISATEURS ---

# Endpoint pour créer un utilisateur
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        password=data['password'],
        genre=data['genre']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur créé avec succès'}), 201


# Endpoint pour lister les utilisateurs
@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'nom': user.nom,
        'prenom': user.prenom,
        'email': user.email,
        'genre': user.genre
    } for user in users]), 200


# Endpoint pour afficher un seul utilisateur
@bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'Utilisateur introuvable'}), 404
    return jsonify({
        'id': user.id,
        'nom': user.nom,
        'prenom': user.prenom,
        'email': user.email,
        'genre': user.genre
    }), 200


# Endpoint pour mettre à jour un utilisateur
@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'Utilisateur introuvable'}), 404
    user.nom = data.get('nom', user.nom)
    user.prenom = data.get('prenom', user.prenom)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.genre = data.get('genre', user.genre)
    
    db.session.commit()
    return jsonify({'message': 'Utilisateur mis à jour avec succès'}), 200


# Endpoint pour supprimer un utilisateur
@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'Utilisateur introuvable'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur supprimé avec succès'}), 200


# --- DÉPENSES ---

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


# Endpoint pour mettre à jour une dépense
@bp.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    data = request.get_json()
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({'error': 'Dépense introuvable'}), 404
    expense.date = datetime.strptime(data.get('date', expense.date.strftime('%Y-%m-%d')), '%Y-%m-%d')
    expense.description = data.get('description', expense.description)
    expense.categorie = data.get('categorie', expense.categorie)
    expense.montant = data.get('montant', expense.montant)
    db.session.commit()
    return jsonify({'message': 'Dépense mise à jour avec succès'}), 200


# Endpoint pour supprimer une dépense
@bp.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({'error': 'Dépense introuvable'}), 404
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Dépense supprimée avec succès'}), 200


# --- REVENUS ---

# Endpoint pour créer un revenu
@bp.route('/incomes', methods=['POST'])
def create_income():
    data = request.get_json()
    income = Income(
        user_id=data['user_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        description=data['description'],
        status=data['status'],
        categorie=data['categorie'],
        montant=data['montant']
    )
    db.session.add(income)
    db.session.commit()
    return jsonify({'message': 'Revenu ajouté avec succès'}), 201


# Endpoint pour lister les revenus d'un utilisateur
@bp.route('/incomes/<int:user_id>', methods=['GET'])
def get_incomes(user_id):
    incomes = Income.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': income.id,
        'date': income.date.strftime('%Y-%m-%d'),
        'description': income.description,
        'status': income.status,
        'categorie': income.categorie,
        'montant': income.montant
    } for income in incomes]), 200


# Endpoint pour mettre à jour un revenu
@bp.route('/incomes/<int:id>', methods=['PUT'])
def update_income(id):
    data = request.get_json()
    income = Income.query.get(id)
    if not income:
        return jsonify({'error': 'Revenu introuvable'}), 404
    income.date = datetime.strptime(data.get('date', income.date.strftime('%Y-%m-%d')), '%Y-%m-%d')
    income.description = data.get('description', income.description)
    income.status = data.get('status', income.status)
    income.categorie = data.get('categorie', income.categorie)
    income.montant = data.get('montant', income.montant)
    db.session.commit()
    return jsonify({'message': 'Revenu mis à jour avec succès'}), 200


# Endpoint pour supprimer un revenu
@bp.route('/incomes/<int:id>', methods=['DELETE'])
def delete_income(id):
    income = Income.query.get(id)
    if not income:
        return jsonify({'error': 'Revenu introuvable'}), 404
    db.session.delete(income)
    db.session.commit()
    return jsonify({'message': 'Revenu supprimé avec succès'}), 200
