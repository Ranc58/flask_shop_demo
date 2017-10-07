from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_model = db.Column(db.Text)
    product_path = db.Column(db.String(64))
    product_color = relationship('Color')
    processor_model = db.Column(db.String(64))
    processor_frequency = db.Column(db.Integer)
    ram_value = db.Column(db.Integer)
    hdd_value = relationship('Hdd')
    display_size = db.Column(db.Float)
    videocard = db.Column(db.String(128))
    video_memory_value = db.Column(db.Integer)
    weight = db.Column(db.Float)
    optical_drive = db.Column(db.Boolean)
    lte_4g = db.Column(db.Boolean)
    bluetooth = db.Column(db.Boolean)
    wi_fi = db.Column(db.Boolean)
    price = db.Column(db.Integer)


class Color(db.Model):
    __tablename__ = 'colors'
    color_id = db.Column(db.Integer, primary_key=True)
    parent_product_id = db.Column(db.Integer, ForeignKey('products.product_id'))
    product_color = db.Column(db.String(32))


class Hdd(db.Model):
    __tablename__ = 'hdd'
    hdd_id = db.Column(db.Integer, primary_key=True)
    parent_product_id = db.Column(db.Integer, ForeignKey('products.product_id'))
    hdd_value = db.Column(db.Integer)