from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qnty = db.Column(db.Integer)

    def __init__(self, name, description, price, qnty):
        self.name = name 
        self.description = description 
        self.price = price 
        self.qnty = qnty

# ProductSchema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qnty')

# init schema 
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# create a product 
@app.route('/product', methods=["POST"])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qnty = request.json["qnty"]

    new_product = Product(name, description, price, qnty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

if __name__ == "__main__":
    app.run(debug=True)