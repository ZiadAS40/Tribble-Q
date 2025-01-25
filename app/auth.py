#!usr/bin/python3

from flask import request, jsonify, flash, Blueprint, render_template, redirect, url_for

from flask_login import login_user, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """Login"""
    from app.models.user import User
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=user_name).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f"welcome {user.username}", 'success')
            return redirect(url_for('home'))
        flash('invalid username or password', 'error')
        return redirect(url_for('auth.login'))
    return render_template('login.html')


@auth.route('/logout', methods=['POST'], strict_slashes=False)
def logout():
    """Logout"""
    logout_user()
    return redirect(url_for('home'))

@auth.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    """Register"""
    from app.models.user import User
    if request.method == 'POST':
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user_with_email = User.query.filter_by(email=email).first()
        user_with_username = User.query.filter_by(username=user_name).first()

        if user_with_username:
            flash('the user name already exist', 'error')
            return redirect(url_for('auth.signup'))

        if user_with_email:
            flash(f"email address already exitst\nplease choose different email", 'error')
            return redirect(url_for('auth.signup'))

        if password != confirm_password:
            flash('password do not match', 'error')
            return redirect(url_for('auth.signup'))

        user_dict = {}
        user_dict['username'] = user_name
        user_dict['email'] = email
        user_dict['password'] = password
        print(user_dict)
        user = User(**user_dict)
        user.save()
        return redirect(url_for('auth.login'))
    return render_template('signup.html')