from curses import flash
from flask import Flask, render_template, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Message, Mail
#from app import  mail

from .extensions import db
from .forms import ContactForm
from .models import User, Role, Project
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
# Register 'zip' as a Jinja filter
app.jinja_env.filters['zip'] = zip


# Initialise extensions
db.init_app(app)
mail=Mail()
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create database tables before first request (Flask 3.0 compatible)
with app.app_context():
    db.create_all()
    if not user_datastore.find_user(email="admin@example.com"):
        user_datastore.create_user(
            email="admin@example.com",
            password="password123",  # will be hashed by Flask-Security
        )
        db.session.commit()


