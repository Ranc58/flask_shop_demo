from flask import Flask, render_template
from models import db, Product


app = Flask(__name__)
app.config.from_object('config')
db.app = app
db.init_app(app)


@app.route('/')
def products_catalog():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/product/<product_id>')
def product_info(product_id=None):
    product = Product.query.filter_by(product_id=product_id).first()
    return render_template('product.html', product=product)


if __name__ == "__main__":
    app.run(debug=True) #TODO Del