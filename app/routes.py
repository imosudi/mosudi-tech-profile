from flask import render_template, redirect, url_for, flash
from flask_mail import Message

from . import app, mail

from .forms import ContactForm
from .models import Project


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
            recipients=["info@serverafrica.com"],
            body=f"From: {form.name.data} <{form.email.data}>\n\n{form.message.data}",
        )
        mail.send(msg)
        flash("Thank you! Your message has been sent successfully.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)


