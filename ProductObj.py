#ProductObj.py
from datetime import datetime
import json


class Product:
    product_id = -1;
    name = ""
    description = ""
    price = 0.0
    createdDate = ""

    @staticmethod
    def initial(pid, name, description, price):
        product = Product()
        product.init(pid, name, description, price)
        return product

    
    def init(self, pid, name, description, price):
        self.product_id = pid
        self.name = name
        self.description = description
        self.price = price
        self.createdDate = datetime.now().strftime("%m/%d/%YT%H:%M:%S")
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
            
    def getProdcutInfo(self):
        body = { 
             'product_id': self.product_id,
             'name': self.name,
             'description': self.description,
             'price': self.price,
             'created_date': self.createdDate,
        }
        
        return body