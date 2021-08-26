from app.models import User, Product
from flask import render_template, abort,flash, request, redirect,url_for
from .. import db, photos
from . import main
from flask_login import login_required, current_user
from .forms import Product_Form

@main.route('/')
def index():

    title= 'Welcome to Kreative Brands'
    return render_template('index.html', title = title)

@main.route('/about')
def about():
    tittle = 'About Kreative Brands'
    return render_template('about.html', tittle = tittle)

@main.route('/tshirt')
def tshirt():
    tittle = 'Tshirts'
    return render_template('tshirt.html', tittle = tittle)

@main.route('/shoes')
def shoes():
    tittle = 'Shoes'
    return render_template('shoes.html', tittle = tittle)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    message = Product.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=message)

@main.route('/admin/add', methods = ["GET","POST"])
def add_product():
    form = Product_Form()

    if form.validate_on_submit():
        product = Product(name = form.name.data, category= form.category.data, description= form.description.data ,price = form.price.data)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('main.index'))
    tittle = 'New Product'
    return render_template('newproduct.html', tittle = tittle, addProduct_form = form)

@main.route('/admin/add_photo', methods = ["GET","POST"])
def update_photo():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        Product.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('update-pic.html')
