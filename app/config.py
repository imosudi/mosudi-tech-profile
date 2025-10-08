import os, time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Core Flask configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mosudi_tech_profile.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Security-Too configuration
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "default-salt")
    SECURITY_REGISTERABLE = os.getenv("SECURITY_REGISTERABLE", "True") == "True"
    SECURITY_SEND_REGISTER_EMAIL = os.getenv("SECURITY_SEND_REGISTER_EMAIL", "False") == "True"

    # Optional: Email configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER", "localhost")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "False") == "True"
    MAIL_PORT = int(os.getenv("MAIL_PORT", 25))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "False") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
