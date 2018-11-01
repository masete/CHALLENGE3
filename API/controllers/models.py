class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

        
class Product:
    def __init__(self,product_id, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def to_json(self):
        product = {
        "product_id": self.product_id,
        "product_name" : self.product_name,
        "product_price" : self.product_price
         }
        return product


class Sale:
    def __init__(self,sale_id, sale_quantity, sale_price):
        self.sale_quantity = sale_quantity
        self.sale_price = sale_price

    def format_to_json(self):
        sale = {
        "sale_id":self.sale_id,
        "sale_quantity" : self.sale_quantity,
        "sale_price" : self.sale_price
         }
        return product




        