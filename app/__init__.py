import os
from flask import Flask, render_template
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from .extensions import db
from .models import User, Role
from .config import Config

# Instantiate Flask app directly
app = Flask(__name__)
app.config.from_object(Config)

# Register Jinja filter
app.jinja_env.filters['zip'] = zip

# Initialise extensions
db.init_app(app)
mail = Mail(app)

# Flask-Security setup
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create database tables
with app.app_context():
    db.create_all()
    if not user_datastore.find_user(email="admin@example.com"):
        user_datastore.create_user(
            email="admin@example.com",
            password="password123",  # auto-hashed
        )
        db.session.commit()

# Import routes after app setup to avoid circular import
from . import routes, errors # noqa: E402

