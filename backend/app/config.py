import os
from dotenv import load_dotenv

load_dotenv()  # Charge le .env automatiquement

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clerk (auth)
    CLERK_JWT_ISSUER = os.getenv("CLERK_JWT_ISSUER")
    CLERK_JWT_PUBLIC_KEY_URL = os.getenv("CLERK_JWT_PUBLIC_KEY_URL")
    CLERK_JWT_AUDIENCE = os.getenv("CLERK_JWT_AUDIENCE")
