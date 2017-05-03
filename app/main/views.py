from flask import render_template, redirect, url_for
from datetime import timedelta
from functools import update_wrapper
from . import main
from .forms import ContactForm
from ..email import send_email
from flask_cors import cross_origin


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about/')
def about():
    return render_template('about.html')


@main.route('/services/')
def services():
    return render_template('services.html')


@main.route('/projects')
def projects():
    return render_template('projects.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email("sperk434@gmail.com", 'New Inquiry', 'mail/contact', name=form.name.data, email=form.email.data, message=form.message.data)
        return redirect(url_for('main.index'))
    return render_template('contact.html', form=form)
