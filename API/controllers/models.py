class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

        
class Product:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price


class Sale:
    def __init__(self, sale_quantity, sale_price):
        self.sale_quantity = sale_quantity
        self.sale_price = sale_price


        