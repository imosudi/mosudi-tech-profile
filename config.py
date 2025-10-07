import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'replace-with-strong-secret')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'mosudi_profile.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Security config
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'change-me-salt')
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None

    # Flask-Mail (optional for later)
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_DEFAULT_SENDER = 'noreply@mioemi.com'
    MAIL_SUPPRESS_SEND = True
