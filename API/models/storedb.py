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
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL

                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "products" (                    
                    products_id SERIAL PRIMARY KEY,
                    product_name VARCHAR(20) NOT NULL,
                    product_price INTEGER NOT NULL                                  
                    
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "sales" (
                    sales_id SERIAL PRIMARY KEY,
                    products_id INT REFERENCES products(products_id),
                    user_id INT REFERENCES users(user_id),
                    sale VARCHAR(100)
                )
            """,)

        try:
            if(os.getenv("FLASK_ENV")) == "Production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            else:
                self.connection = psycopg2.connect(dbname='store',
                                                   user='postgres',
                                                   password='masete',
                                                   host='localhost',
                                                   port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            for command in commands:
                self.cursor.execute(command)
        except(Exception, psycopg2.DatabaseError) as error:
            raise error

    def insert_new_product(self, user_id, added_product):
        """
           Method for adding a new product to the database
        """
        self.cursor.execute("SELECT * FROM products WHERE products = %s", [added_product])
        check_product = self.cursor.fetchone()
        if check_product:
            return "product exits "
        
        insert_product = "INSERT INTO products(product_id, product_name, product_price ) VALUES('"+product_id+"', '"+product_name[0]+"', '"+added_product+"')"
        self.cursor.execute(insert_product)
        return "product succcssfully created"

   