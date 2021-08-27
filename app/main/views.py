from itertools import product
from app.models import Order, User, Product
from flask import render_template, abort,flash, request, redirect,url_for
from .. import db, photos
from . import main
from flask_login import login_required, current_user
from .forms import Product_Form,Order_Form
from ..email import mail_message

@main.route('/')
def index():
    products = Product.query.all()

    title= 'Welcome to Kreative Brands'
    return render_template('index.html', title = title, products=products)

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

@main.route('/admin/add', methods = ["GET","POST"])
def add_product():
    form = Product_Form()
    if form.validate_on_submit():
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            product = Product( image_path = path , name = form.name.data, category= form.category.data, description= form.description.data ,price = form.price.data)
            db.session.add(product)
            db.session.commit()

        return redirect(url_for('main.index'))
    tittle = 'New Product'
    return render_template('newproduct.html', tittle = tittle, addProduct_form = form)

@main.route('/order', methods = ["GET","POST"])
def order_product():
    form = Order_Form()
    if form.validate_on_submit():
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            order = Order(image_path = path, category= form.category.data, quantity= form.quantity.data, description= form.description.data , phone = form.phone.data , pod = form.pod.data, name = form.name.data , email= form.email.data)
            db.session.add(order)
            db.session.commit()


        mail_message("Welcome to Kreative Brands","email/order_user", order.email, order=order)
        return redirect(url_for('main.index'))
    title = 'Checkout'
    return render_template('orderproduct.html', tittle = title, orderProduct_form = form)

