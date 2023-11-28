__author__ = 'phemananth'

from flask import Flask, jsonify, request

 
from Products import ProductList
from ProductObj import Product

app = Flask(__name__)

@app.route("/")
def IamWorking():
    return "I'm Okay!"


products = ProductList()

@app.route("/product", methods=['POST'])
def addProducts():
	print("Add Products")
	data = request.json
	product = Product()
	product.init(data)
	products.addProduct(product)
	return {"status":200,"description":"Product is created"}

@app.route("/product", methods=['GET'])
def getAllProducts():
	print("getAllProducts")
	data =  {"products": products.getAllProduct()}
	return jsonify(data)
