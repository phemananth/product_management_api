__author__ = 'Vignesh Kumar'

from flask import Flask, jsonify, make_response, request
from flask_httpauth import HTTPTokenAuth


 
from Products import ProductList
from ProductObj import Product
from Auth_Middleware import token_required


app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = ["vigesh","hello"]

@app.route('/')
def index():
    return "Hello, {}!".format(auth.current_user())


products = ProductList()

@app.route("/product", methods=['POST'])
@token_required
def addProducts():
	data = request.json
	product = Product.initial(data["product_id"],data["name"],data["description"],data["price"])
	products.addProduct(product)
	return {"status":200,"description":"Product is created"}

@app.route("/product", methods=['GET'])
def getAllProducts():
	print("getAllProducts")
	data =  {"products": products.getAllProduct()}
	return jsonify(data)
