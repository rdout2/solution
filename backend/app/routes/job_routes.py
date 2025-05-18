from flask import Blueprint, jsonify, request
from app.modeles.application import Application
from app.db import db

job_bp = Blueprint('job_bp', __name__)

# Ping test
@job_bp.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong ! L’API fonctionne ✅"}), 200

# 🔍 Lister toutes les candidatures
@job_bp.route('/api/applications', methods=['GET'])
def get_all_applications():
    applications = Application.query.all()
    return jsonify([app.to_dict() for app in applications]), 200

# ➕ Ajouter une nouvelle candidature
@job_bp.route('/api/applications', methods=['POST'])
def add_application():
    data = request.get_json()
    try:
        new_app = Application(
            title=data['title'],
            company=data['company'],
            status=data.get('status', 'Wishlist'),
            date_applied=data.get('date_applied'),
            job_board=data.get('job_board'),
            location=data.get('location'),
            notes=data.get('notes')
        )

        db.session.add(new_app)
        db.session.commit()
        return jsonify(new_app.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✏️ Modifier une candidature
@job_bp.route('/api/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    app = Application.query.get_or_404(app_id)
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

# ❌ Supprimer une candidature
@job_bp.route('/api/applications/<int:app_id>', methods=['DELETE'])
def delete_application(app_id):
    app = Application.query.get_or_404(app_id)
    db.session.delete(app)
    db.session.commit()
    return jsonify({"message": f"Candidature {app_id} supprimée ✅"}), 200
