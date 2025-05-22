FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . /app/

# Exposer le port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "run.py"]
