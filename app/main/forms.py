from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    message = TextAreaField('Message', validators=[Required()])
    submit = SubmitField('Submit')
