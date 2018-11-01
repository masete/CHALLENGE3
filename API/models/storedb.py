"""
   database setup for supporting endpoints functionality
"""
import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    """
       Class containing our database queries..
    """
    def __init__(self):
        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL

                )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (                    
                    products_id SERIAL PRIMARY KEY,
                    product_name VARCHAR(20) NOT NULL,
                    product_price INTEGER NOT NULL                                  
                    
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS sales (
                    sale_id SERIAL PRIMARY KEY,
                    sale_price INTEGER NOT NULL,
                    sale_quantity INTEGER NOT NULL
                )
            """,)

        self.connection = psycopg2.connect(dbname='store',
                                            user='postgres',
                                            password='masete',
                                            host='localhost',
                                                port='5432')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory = RealDictCursor)
        print(self.cursor)
        for command in self.commands:
            self.cursor.execute(command)


    def signup(self,user_name,email,password):

        insert_user = "INSERT INTO users(user_name,email,password) VALUES('{}','{}','{}')".format(user_name,email,password)
        self.cursor.execute(insert_user)
        return "user added"

    def login(self,user_name):
        login_user = "SELECT * FROM users WHERE user_name = {}".format(user_name)
        self.cursor.execute(login_user)
        return self.cursor.fetchone()

    def get_product_by_name(self, product_name):

        productbyname = "SELECT * FROM products WHERE product_name = {}".format(str(product_name))
        self.cursor.execute(productbyname)
        return self.cursor.fetchone()
    
    def get_product_by_id(self, product_id):

        productbyid = "SELECT * FROM products WHERE products_id = {}".format(product_id)
        self.cursor.execute(productbyid)
        return self.cursor.fetchone()


    def insert_new_product(self,product_name, product_price):

        insert_product = "INSERT INTO products(product_name, product_price ) VALUES('{}','{}')".format(product_name,product_price)
        self.cursor.execute(insert_product)
        return "product successfully created"

    def get_all_products(self):

        get_product = "SELECT * FROM products"
        self.cursor.execute(get_product)
        return self.cursor.fetchall()

        get_product = product('{}','{}','{}')

    
    def get_one_product(self, product_id):

        get_single_product = "SELECT * FROM products WHERE products_id = {}".format(product_id)
        self.cursor.execute(get_single_product)
        return self.cursor.fetchone()

    def modify_product(self,products_id,product_name,product_price):
        modify = "UPDATE products SET product_name = '{}', product_price = '{}' WHERE products_id = {}".format(product_name,product_price,products_id)
        self.cursor.execute(modify)

    def delete_product(self,products_id):
        delete = "DELETE FROM products WHERE products_id = {}".format(int(products_id))
        self.cursor.execute(delete)

    def insert_new_sale(self,sale_quantity, sale_price):

        insert_sale = "INSERT INTO sales(sale_quantity, sale_price ) VALUES('{}','{}')".format(sale_quantity,sale_price)
        self.cursor.execute(insert_sale)
        return "product succcssfully created"

    def get_all_sales(self):

        get_sale = "SELECT * FROM sales"
        self.cursor.execute(get_sale)
        return self.cursor.fetchall()

    def get_one_sale(self, sale_id):

        get_single_sale = "SELECT * FROM sales WHERE sale_id = {}".format(sale_id)
        self.cursor.execute(get_single_sale)
        return self.cursor.fetchone()

   