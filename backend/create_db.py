from app import create_app
from app.db import db
from app.modeles.application import Application

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tables créées avec succès.")
