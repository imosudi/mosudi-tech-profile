from flask import Flask, render_template, redirect, url_for, flash
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
mail=Mail(app)
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



# Routes
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', title='Home', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html', title='About Me')

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', title='Projects', projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Example: send email (optional)
        msg = Message(
            subject=f"[Portfolio] {form.subject.data}",
            sender=form.email.data,
            recipients=["imosudi@gmail.com"],
            body=f"From: {form.name.data} <{form.email.data}>\n\n{form.message.data}",
        )
        mail.send(msg)
        flash("Thank you! Your message has been sent successfully.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

@app.route('/debug-mail')
def debug_mail():
    print(
        'server:', app.config.get('MIO_MAIL_SERVER'),
            'port: ', app.config.get('MIO_MAIL_PORT'),
            'use_tls: ',  app.config.get('MIO_MAIL_USE_TLS'),
            'use_ssl: ', app.config.get('MIO_MAIL_USE_SSL'),
            'username,' , app.config.get('MIO_MAIL_USERNAME'),
            'password_set: ', bool(app.config.get('MIO_MAIL_PASSWORD')))
    #if app.debug:  # Only in development!
    return {
            'server': app.config.get('MIO_MAIL_SERVER'),
            'port': app.config.get('MIO_MAIL_PORT'),
            'use_tls': app.config.get('MIO_MAIL_USE_TLS'),
            'use_ssl': app.config.get('MIO_MAIL_USE_SSL'),
            'username': app.config.get('MIO_MAIL_USERNAME'),
            'password_set': bool(app.config.get('MIO_MAIL_PASSWORD'))
        }
    return "Not available", 403

# Error handlers
@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
