import os, time

from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables from .env file
#load_dotenv()
dotenv_path = join(dirname(__file__), '.env')
#print(dotenv_path); time.sleep(300)
load_dotenv(dotenv_path)

#print(os.getenv("MIO_SECRET_KEY")); time.sleep(300)
class Config:
    # Core Flask configuration
    SECRET_KEY = os.getenv("MIO_SECRET_KEY", "default-secret-key")
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("MIO_DATABASE_URL", "sqlite:///mosudi_tech_profile.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Security-Too configuration
    SECURITY_PASSWORD_SALT = os.getenv("MIO_SECURITY_PASSWORD_SALT", "default-salt")
    SECURITY_REGISTERABLE = os.getenv("MIO_SECURITY_REGISTERABLE", "True") == "True"
    SECURITY_SEND_REGISTER_EMAIL = os.getenv("SECURITY_SEND_REGISTER_EMAIL", "False") == "True"

    # Optional: Email configuration
    MIO_MAIL_SERVER = os.getenv("MIO_MAIL_SERVER", "localhost")
    MIO_MAIL_USE_SSL = os.getenv("MIO_MAIL_USE_SSL", "False") == "True"
    MIO_MAIL_PORT = int(os.getenv("MIO_MAIL_PORT", 25))
    MIO_MAIL_USE_TLS = os.getenv("MIO_MAIL_USE_TLS", "False") == "True"
    MIO_MAIL_USERNAME = os.getenv("MIO_MAIL_USERNAME")
    MIO_MAIL_PASSWORD = os.getenv("MIO_MAIL_PASSWORD")

