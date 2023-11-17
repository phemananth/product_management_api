__author__ = 'phemananth'

import json


#Products.py

class ProductList:
    productList = []

    # Add the product to the Table
    def addProduct(self, product):
        self.productList.append(product)
        print(f'{product.getProdcutInfo()} len {len(self.productList)}')

    # Get All the products
    def getAllProduct(self):
        products = []
        for prod in self.productList:
            products.append(prod.getProdcutInfo())

        return products
        
    # Get All the products
    def getProductByID(self, pid):
        products = []
        for prod in self.productList:
            if prod.product_id == pid:
                print(f'{prod.getProdcutInfo()}')
                products.append(prod)
        return products
        
    # Update Product by ID
    def updateProductByID(self, pid, name):
        index = 0
        for prod in self.productList:
            if prod.product_id == pid:
                prod.name = name
                self.productList[index] = prod
                print(f'{prod.getProdcutInfo()}')
            index = index+1
    
     # Delete products by ID
    def deleteProductByID(self, pid):
        index = 0
        for prod in self.productList:
            if prod.product_id == pid:
                self.productList.remove(prod)
                print(f'{prod.getProdcutInfo()}')
            index = index+1

    
