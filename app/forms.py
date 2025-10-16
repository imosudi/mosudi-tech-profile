from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class Contact_Form_(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired(), Length(min=3, max=150)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Send Message")

class ContactForm__(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    
    # Optional dropdown subject options
    subject_choice = SelectField(
        "Subject Category (Optional)",
        choices=[
            ("", "Select a category..."),
            ("project", "Project Collaboration"),
            ("research", "Research Partnership"),
            ("career", "Career / Mentorship"),
            ("consult", "Consultation / Advisory"),
            ("other", "Other"),
        ],
        validators=[Optional()]
    )

    subject = StringField("Subject or Topic", validators=[Optional(), Length(max=100)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Send Message")



class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    
    subject_choice = SelectField(
        "Subject Category (Optional)",
        choices=[
            ("", "Select a category..."),
            ("project", "Project Collaboration"),
            ("research", "Research Partnership"),
            ("career", "Career / Mentorship"),
            ("consult", "Consultation / Advisory"),
            ("other", "Other"),
        ],
        validators=[Optional()]
    )

    subject = StringField("Subject or Topic", validators=[Optional(), Length(max=100)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])

    # ✅ Add Google reCAPTCHA v2
    recaptcha = RecaptchaField()

    submit = SubmitField("Send Message")