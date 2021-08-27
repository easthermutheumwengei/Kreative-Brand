from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, PasswordField,SubmitField, ValidationError,SelectField, TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class Order_Form(FlaskForm):
    category = SelectField('Select Product', choices=[('Mug','Mug'),('Hoodie','Hoodie'),('Tshirt','Tshirt'),('Tshirt','Tshirt')],validators=[Required()])
    quantity = StringField('How many selected items do you need?',validators = [Required()])
    description = StringField('Kindly describe how you want us to brand your above product',validators = [Required()])
    pod= SelectField('Which method will you prefer?', choices=[('Pay on delivery','Pay on delivery'),('Deposit 50% and pay the rest on delivery','Deposit 50% and pay the rest on delivery')],validators=[Required()])
    name=StringField('Name',validators = [Required()])
    phone= StringField('PLease enter the phone number to reach you out.',validators = [Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Order')

class Product_Form(FlaskForm):
    name = SelectField('Select Product', choices=[('Mug','Mug'),('Hoodie','Hoodie'),('Tshirt','Tshirt')],validators=[Required()])
    category = SelectField('Select Category', choices=[('Kitchen', 'Kitchenware'),('Upper', 'Upperbody Apparel'),('Upper', 'Lowerbody Apparel')],validators=[Required()])
    price = StringField('The price',validators = [Required()])
    description = StringField('Add relevant description',validators = [Required()])
    submit = SubmitField('Add Product')