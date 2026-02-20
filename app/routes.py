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

@app.route('/portfolio')
def portfolio():
    projects = Project.query.all()
    return render_template('portfolio.html', title='Portfolio', projects=projects)

@app.route("/contact",  methods=["GET", "POST"])
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

    return render_template("contact.html",title='Contact', form=form, RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY)

@app.route('/services')
def services():
    return render_template('services.html', title='My Services')


@app.route("/network-infrastructure")
def network_infra():
    return render_template("projects/project_enterprise_network.html", title="Enterprise Network Infrastructure")    

@app.route("/icinga2-monitoring-system")
def infra_monitoring():
    return render_template("projects/icinga2.html", title="Icinga2 Monitoring System")

@app.route("/kvm_virtualisation")
def kvm_gluster_infra():
    return render_template("projects/kvm_virtualisation.html", title="Icinga2 Monitoring System")

@app.route("/point-to-point")
def point_to_point():
    return render_template("projects/point-to-point.html", title="Point to Point Wireless Link")

@app.route("/gallery")
def gallery():

    api_project_images = [
        ("IMG_20220301_153402_6.jpg", 2080, 4160),
        ("IMG_20220301_153421_5.jpg", 4160, 2080),
        ("IMG_20220301_153444_1.jpg", 4160, 2080),
        ("IMG_20220301_153559_8.jpg", 4160, 2080),
        ("IMG_20220302_114137_6.jpg", 2448, 3264),
        ("IMG_20220302_114145_4.jpg", 2448, 3264),
        ("IMG_20220302_125805_1.jpg", 4160, 2080),
        ("IMG_20220302_125831_6.jpg", 2080, 4160),
        ("IMG_20220302_125900_7.jpg", 2080, 4160),
        ("IMG_20220302_130131_8.jpg", 2080, 4160),
        ("IMG_20220302_130159_9.jpg", 2080, 4160),
        ("IMG_20220302_130228_7.jpg", 4160, 2080),
        ("IMG_20220302_130246_9.jpg", 2080, 4160),
        ("IMG_20220303_095640_1.jpg", 2080, 4160),
        ("IMG_20220303_095728_5.jpg", 2080, 4160),
    ]

    training_images = [
        ("IMG_20170728_123227.jpg", 1600, 1200),
        ("img_20170801_171500_1024.jpg", 1024, 768),
        ("img_20170801_171506_1024.jpg", 1024, 768),
        ("img_20170801_171514_1024.jpg", 1024, 768),
        ("img_20170801_171523.jpg", 4032, 3024),
        ("img_20170801_171529_1024.jpg", 768, 1024),
        ("img_20170801_171529.jpg", 3024, 4032),
        ("IMG_20170801_180555.jpg", 4032, 3024),
        ("IMG_20170801_180650.jpg", 4032, 3024),
        ("IMG_20170801_180654.jpg", 4032, 3024),
    ]

    network_images = [
        ("IMG_20210122_183531_6.jpg", 2448, 3264),
        ("IMG_20210122_183542_5.jpg", 2448, 3264),
        ("IMG_20210123_102605_4.jpg", 2080, 4160),
        ("IMG_20210123_102626_8.jpg", 2080, 4160),
        ("IMG_20210123_102754_9.jpg", 2448, 3264),
        ("IMG_20210123_103002_2.jpg", 2448, 3264),
        ("IMG_20210123_103015_0.jpg", 2448, 3264),
        ("IMG_20210125_083711_4.jpg", 1632, 3264),
        ("IMG_20210125_084046_9.jpg", 1632, 3264),
        ("IMG_20210212_154832_7.jpg", 2080, 4160),
        ("IMG_20210212_154853_4.jpg", 2080, 4160),
        ("IMG_20210212_155011_5.jpg", 2080, 4160),
        ("IMG_20210212_155030_1.jpg", 2080, 4160),
        ("IMG_20250104_114219_4.jpg", 3120, 4160),
        ("IMG_20250223_182456_556.jpg", 3120, 4160),
        ("IMG_20250223_182507_034.jpg", 3120, 4160),
        ("IMG_20250223_182511_500.jpg", 3120, 4160),
        ("IMG_20250223_182610_263.jpg", 3120, 4160),
        ("IMG_20250225_192254_894.jpg", 3120, 4160),
        ("IMG_20250320_114944_483.jpg", 1728, 3072),
        ("IMG_20250320_115123_753.jpg", 1728, 3072),
        ("IMG_20250320_115155_960.jpg", 1728, 3072),
        ("IMG_20250320_115220_721.jpg", 1728, 3072),
        ("IMG_20250320_120100_559.jpg", 1728, 3072),
        ("IMG_20250320_120138_924.jpg", 1728, 3072),
    ]

    return render_template(
        "gallery.html",
        title="Gallery",
        api_project_images=api_project_images,
        training_images=training_images,
        network_images=network_images
    )



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