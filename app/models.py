from flask_login import login_manager, login_user, UserMixin
from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    user_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    product = db.relationship('Product', backref='user', lazy='dynamic')
    order = db.relationship('Order', backref='user', lazy='dynamic')
    
    
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')
    @set_password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.user_password,password) 
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'
class Product(UserMixin, db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    price = db.Column(db.Text(), nullable = False)
    description = db.Column(db.String(255),nullable = False)
    category= db.Column(db.String(255),nullable = False)
    image_path = db.Column(db.String())
    orders = db.relationship('Order',backref='product',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    
    
    def save_Product(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'Product {self.post}'
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text(),nullable = False)
    quantity = db.Column(db.Text(),nullable = False)
    description = db.Column(db.Text(),nullable = False)
    pod = db.Column(db.Text(),nullable = False)
    name = db.Column(db.Text(),nullable = False)
    phone = db.Column(db.Text(),nullable = False)
    email = db.Column(db.Text(),nullable = False)
    image_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable = True)
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'), nullable = True)
    def add_oredr(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_order(cls,product_id):
        order = Order.query.filter_by(product_id= id).all()
        return order
    def __repr__(self):
        return f'Order:{self.order}'
