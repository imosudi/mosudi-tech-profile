import os
from flask import render_template, redirect, url_for, flash
from flask_mail import Message

from app.config import RECAPTCHA_SITE_KEY
from . import app, mail
from .extensions import db
from .forms import ContactForm
from .models import Project


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
        try:
            subject_category = dict(form.subject_choice.choices).get(form.subject_choice.data, "")
            subject_text = form.subject.data.strip() or subject_category or "General Enquiry"

            msg = Message(
                subject=f"[Portfolio] {subject_text}",
                sender=os.getenv('MIO_MAIL_DEFAULT_SENDER', 'info@mioemi.com'),
                recipients=["info@mioemi.com"],
                body=f"From: {form.name.data} <{form.email.data}>\n\n{form.message.data}",
                reply_to=form.email.data
            )
            mail.send(msg)
            flash("Thank you! Your message has been sent successfully.", "success")
            #return redirect(url_for("contact"))
            return redirect(url_for("index"))  # ✅ Go back home
        except Exception as e:
            print(f"Error sending email: {e}")
            flash("Sorry, there was an error sending your message. Please try again.", "error")

    return render_template("contact.html", form=form, RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY)


@app.route("/message-sent")
def message_sent():
    return render_template("message_sent.html")


@app.route('/debug-mail')
def debug_mail():
    """Shows mail configuration for debugging (development only)."""
    """if app.debug:
        return {
            'server': app.config.get('MIO_MAIL_SERVER'),
            'port': app.config.get('MIO_MAIL_PORT'),
            'use_tls': app.config.get('MIO_MAIL_USE_TLS'),
            'use_ssl': app.config.get('MIO_MAIL_USE_SSL'),
            'username': app.config.get('MIO_MAIL_USERNAME'),
            'password_set': bool(app.config.get('MIO_MAIL_PASSWORD'))
        }"""
    return "Not available", 403
# Note: Admin routes for managing projects would go here, protected by authentication.  
# These are omitted for brevity and focus on the main public routes.    
# You can implement them using Flask-Security or Flask-Login as needed.
# Example:
# from flask_security import login_required, roles_required
# @app.route('/admin')
# @login_required
# @roles_required('admin')
# def admin_dashboard():
#     return render_template('admin/dashboard.html')        
# @app.route('/admin/projects')