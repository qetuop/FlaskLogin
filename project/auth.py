from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # user does not exist or password fails
    if (not user) or (check_password_hash(user.password, password) == False):
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    
    # valid user/password
    login_user(user, remember=remember)  # check for return val? This will return ``True`` if the log in attempt succeeds, and ``False`` if it fails (i.e. because the user is inactive).
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # don't add user if already in DB
    user = User.query.filter_by(email=email).first()

    # redirect back to signup page to try again....error message?
    if user:
        flash('Email already exists')
        return redirect(url_for('auth.signup'))

    # new user, create, hash password
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))