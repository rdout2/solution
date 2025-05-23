from flask import Blueprint, jsonify, request
from app.modeles.application import Application
from app.db import db
from app.utils.clerk import get_clerk_user_id_from_token


job_bp = Blueprint('job_bp', __name__)

# Ping test
@job_bp.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong ! L’API fonctionne ✅"}), 200

# 🔍 Lister toutes les candidatures de l'utilisateur connecté
@job_bp.route('/api/applications', methods=['GET'])
def get_all_applications():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify([]), 200
    token = auth_header.split(" ")[1]
    user_id = get_clerk_user_id_from_token(token)
    if not user_id:
        return jsonify([]), 200
    applications = Application.query.filter_by(user_id=user_id).all()
    return jsonify([app.to_dict() for app in applications]), 200

# ➕ Ajouter une nouvelle candidature pour l'utilisateur connecté
@job_bp.route('/api/applications', methods=['POST'])
def add_application():
    data = request.get_json()
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Unauthorized"}), 401
    token = auth_header.split(" ")[1]
    user_id = get_clerk_user_id_from_token(token)
    if not user_id:
        return jsonify({"error": "Invalid token"}), 401
    try:
        new_app = Application(
            title=data['title'],
            company=data['company'],
            status=data.get('status', 'Wishlist'),
            date_applied=data.get('date_applied'),
            job_board=data.get('job_board'),
            location=data.get('location'),
            notes=data.get('notes'),
            user_id=user_id
        )
        db.session.add(new_app)
        db.session.commit()
        return jsonify(new_app.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✏️ Modifier une candidature (seulement si elle appartient à l'utilisateur)
@job_bp.route('/api/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Unauthorized"}), 401
    token = auth_header.split(" ")[1]
    user_id = get_clerk_user_id_from_token(token)
    if not user_id:
        return jsonify({"error": "Invalid token"}), 401

    app = Application.query.get_or_404(app_id)
    if app.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()
    app.title = data.get('title', app.title)
    app.company = data.get('company', app.company)
    app.status = data.get('status', app.status)
    app.date_applied = data.get('date_applied', app.date_applied)
    app.job_board = data.get('job_board', app.job_board)
    app.location = data.get('location', app.location)
    app.notes = data.get('notes', app.notes)

    db.session.commit()
    return jsonify(app.to_dict()), 200

# ❌ Supprimer une candidature (seulement si elle appartient à l'utilisateur)
@job_bp.route('/api/applications/<int:app_id>', methods=['DELETE'])
def delete_application(app_id):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Unauthorized"}), 401
    token = auth_header.split(" ")[1]
    user_id = get_clerk_user_id_from_token(token)
    if not user_id:
        return jsonify({"error": "Invalid token"}), 401

    app = Application.query.get_or_404(app_id)
    if app.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(app)
    db.session.commit()
    return jsonify({"message": f"Candidature {app_id} supprimée ✅"}), 200

# 🔎 Récupérer une candidature par son id (seulement si elle appartient à l'utilisateur)
@job_bp.route('/api/applications/<int:app_id>', methods=['GET'])
def get_application(app_id):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Unauthorized"}), 401
    token = auth_header.split(" ")[1]
    user_id = get_clerk_user_id_from_token(token)
    if not user_id:
        return jsonify({"error": "Invalid token"}), 401

    app = Application.query.get_or_404(app_id)
    if app.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403
    return jsonify(app.to_dict()), 200
