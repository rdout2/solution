from flask import Blueprint, request, jsonify
from app.modeles.user import User
from app.db import db

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Champs requis manquants"}), 400

    if User.query.filter((User.username == data["username"]) | (User.email == data["email"])).first():
        return jsonify({"error": "Utilisateur déjà existant"}), 409

    new_user = User(username=data["username"], email=data["email"])
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé ✅"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data.get("username")).first()

    if user and user.check_password(data.get("password")):
        return jsonify({"message": "Connexion réussie ✅", "user": user.to_dict()}), 200
    else:
        return jsonify({"error": "Nom d'utilisateur ou mot de passe invalide"}), 401