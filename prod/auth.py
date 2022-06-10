import os
from collections import OrderedDict
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user

import json
from . import db
from .game.client_interface import ClientInterface
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(user_name=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for("auth.jeu", user=current_user))
                # return render_template("settings.html", user=current_user)
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 11:
            flash('Email must be greater than 11 characters.', category='error')
        elif len(user_name) < 2:
            flash('User name must be greater than 1 character.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            new_user = User(email=email, user_name=user_name,password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for("auth.jeu", user=current_user))

    return render_template("sign-up.html", user=current_user)


@auth.route('/settings', methods=['GET', 'POST'])
@login_required
def setting():
    if request.method == 'POST':
        user = current_user
        old_pwd = request.form.get('old_pwd')
        new_pwd = request.form.get('new_pwd1')
        if user:
            if old_pwd == user.password:
                user.password = new_pwd
                db.session.commit()
                result = 'Password modified !'
                return render_template("settings.html", user=current_user, result=result)
        else:
            return render_template("settings.html", user=current_user, result='error')

    return render_template("settings.html", user=current_user)


@auth.route('/jeu', methods=['GET', 'POST'])
@login_required
def jeu():
    return render_template("jeu.html", user=current_user)

@auth.route('/player/<pid>', methods=['GET'])
def send_player(pid):
    return jsonify(ClientInterface.get_player(pid))


@auth.route('/planet/<pid>', methods=['GET'])
def send_planet(pid):
    return jsonify(ClientInterface.get_planet(pid))


@auth.route('/system', methods=['GET'])
def send_system():
    return jsonify(ClientInterface.get_system())


@auth.route('/planet', methods=['POST'])
def getPlanet():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/createfleets', methods=['POST'])
def createFleets():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/createbuilding', methods=['POST'])
def createBuildings():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/visitmoon', methods=['POST'])
def visitMoon():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/visitplanet', methods=['POST'])
def visitPlanet():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/visitsystem', methods=['POST'])
def visitSystem():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/visitgalaxy', methods=['POST'])
def visitGalaxy():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/movebuilding', methods=['POST'])
def moveBuilding():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/movefleets', methods=['POST'])
def moveFleets():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/search', methods=['POST'])
def search():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/destroybuilding', methods=['POST'])
def destroyBuilding():
    datastore = request.json
    return jsonify(datastore)


@auth.route('/ID/<username>', methods=['GET'])
def getId(username):
    user = User.query.filter_by(user_name=username).first()
    return user.id
