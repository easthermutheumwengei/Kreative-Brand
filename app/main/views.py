from app.models import User, Product
from flask import render_template, abort
from . import main
from flask_login import login_required, current_user

@main.route('/')
def index():

    title= 'Welcome to Kreative Brands'
    return render_template('index.html', title = title)

@main.route('/about')
def about():
    tittle = 'About Kreative Brands'
    return render_template('about.html', tittle = tittle)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    message = Product.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=message)