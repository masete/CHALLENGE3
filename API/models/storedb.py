"""
   database setup for supporting endpoints functionality
"""
import os
import psycopg2


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

        try:

            # if(os.getenv("FLASK_ENV")) == "Production":
            #     self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            # else:
            self.connection = psycopg2.connect(dbname='store',
                                                user='postgres',
                                                password='masete',
                                                host='localhost',
                                                    port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print(self.cursor)
            for command in self.commands:
                self.cursor.execute(command)
        except(Exception, psycopg2.DatabaseError) as error:
            raise error

    def insert_new_product(self,product_name, product_price):

        insert_product = "INSERT INTO products(product_name, product_price ) VALUES('{}','{}')".format(product_name,product_price)
        self.cursor.execute(insert_product)
        return "product succcssfully created"

    def get_all_products(self):

        get_product = "SELECT * FROM products"
        self.cursor.execute(get_product)
        return self.cursor.fetchall()
    
    def get_one_product(self):

        get_single_product = "SELECT * FROM products"
        self.cursor.execute(get_single_product)
        return self.cursor.fetchone()

    def insert_new_sale(self,sale_quantity, sale_price):

        insert_sale = "INSERT INTO sales(sale_quantity, sale_price ) VALUES('{}','{}')".format(sale_quantity,sale_price)
        self.cursor.execute(insert_sale)
        return "product succcssfully created"

    def get_all_sales(self):

        get_sale = "SELECT * FROM sales"
        self.cursor.execute(get_sale)
        return self.cursor.fetchall()

   