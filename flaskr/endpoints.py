
from flask import Flask, render_template, redirect, flash, request, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import uuid
from flaskr.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_required
from flaskr.models import User
from flaskr.auth import verify_information, regex_demo

import os

app = Flask(__name__)
sep = os.path.sep



db = SQLAlchemy(app)

# Defines all the routes for the website
routes = Blueprint('routes', __name__)

# Home page route
@routes.route("/")
def home():
    # print(User.query.first().first_name)
    return render_template("home.html")


@routes.route("/about")
def about():
    return render_template("about.html")


@routes.route("/contact")
def contact():
    return render_template("contact.html")


@routes.route("/services")
def services():
    return render_template("services.html")


# Route for the products page
@routes.route("/products")
def products():
    return render_template("products.html")


# Route for the login page
@routes.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # If the user is trying to log in
    if(form.validate_on_submit()):
        print('Login request')
        # Checks the the information in the form is valid
        flash("Login request for user {}".format(form.username.data))
        return redirect(url_for('home'))
    # If the user is opening the webpage
    else:
        return render_template("login.html", form=form)


@routes.route('/logout')
@login_required
def logout():
    print('Logout endpoint in development')


# Route for the register page
@routes.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    # If the user is trying to register
    if(form.validate_on_submit()):
        print('Register request')
        regex_demo(form.firstname.data,
                   form.lastname.data,
                   form.username.data,
                   form.email.data,
                   form.password.data)
        # Checks that the information in the form is valid
        print("valid")
        try:
            # Add the user account into the database
            # db.session.add(User(id=uuid.uuid3(),
            #                     first_name=form.firstname,
            #                     last_name=form.lastname,
            #                     email=form.email,
            #                     username=form.username,
            #                     pass_hash=generate_password_hash(form.password)))
            # db.session.commit()
            flash('User {} registered'.format(form.username.data))
            return redirect(url_for('login'))
        except exc.IntegrityError:
            return 'Some of the information entered clashes with the information in our database'
        except:
            return "There was an issue getting you registered"
        print("invalid")
        flash("Invalid user account")
        return render_template("register.html", form=form)
    # If the user is visiting the webpage
    else:
        return render_template("register.html", form=form)


# Route for 500 errors
@routes.errorhandler(500)
def database_error(e):
    return "500 Error page"


# Route for 404 errors
@routes.errorhandler(404)
def page_not_found(e):
    return "404 Error page"


# Route for registering a user
@routes.route('/add/')
def add_user(form):
    print('Add user endpoint in development')
    return'Add user endpoint in development'


# Route for deleting a user
@routes.route('/delete/')
@login_required
def delete_user():
    print('Delete user endpoint in development')
    return'Delete user endpoint in development'
