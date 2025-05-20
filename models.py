from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    serialize_rules = ('-products.user', '-user_products.user',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    products = db.relationship('Product', back_populates='user', cascade='all, delete-orphan')
    user_products = db.relationship('UserProduct', back_populates='user', cascade='all, delete-orphan')



    def __repr__(self):
        return f'<User {self.id}>'
    
class Product(db.Model,SerializerMixin):
    __tablename__ = 'products'

    serialize_rules = ('-user.products', '-user_products.product',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)  
    category = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', back_populates='products')
    user_products = db.relationship('UserProduct', back_populates='product', cascade='all, delete-orphan')


    def __repr__(self):
        return f'<Product {self.id}>'
    
class UserProduct(db.Model,SerializerMixin):
    __tablename__ = 'user_products'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    

    user = db.relationship("User", back_populates="user_products")
    product = db.relationship("Product", back_populates="user_products")