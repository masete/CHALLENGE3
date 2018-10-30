"""my controllers holding the HTTP requests"""
from flask import Flask, jsonify, request
from API.models.storedb import Database
from API.controllers.models import Product, Sale
from flask_jwt_extended import create_access_token, JWTManager


db = Database()

def start_app():
    """starting  the flask instance"""
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']='jwt-secret-string'
    jwt= JWTManager(app)


    @app.route("/", strict_slashes=False)
    def index():
        return jsonify({"message":"No products are available yet."})
        

    @app.route("/api/auth/signup/", methods=["POST"], strict_slashes=False)
    def signup():

        data = request.get_json()
        user_name = data.get('user_name')
        email = data.get('email')
        password = data.get('password')

        add_user =db.signup(user_name,email,password)
        return jsonify({"user":add_user})


    @app.route("/api/auth/login/", methods=["POST"], strict_slashes=False)
    def login():

         
        data = request.get_json()
        user_name = data.get('user_name')
        password  = data.get('password')

        access_token = create_access_token(identity=user_name)
        return {'access_token':access_token}, 200


 


             
    @app.route("/api/v1/products/", methods=["POST"], strict_slashes=False)
    def post_a_product():
        """params: none, post a product by postman"""
        try:
        
            feedback = request.get_json()
            product_name = feedback['product_name']
            product_price = feedback['product_price']
            new_product = Product(product_name, product_price)

            # if product_name == " ":
            #     return jsonify({"message":"Product field can not have space"}), 400
            # if product_name == "":
            #     return jsonify({"message":"Product field can not be empty"}), 400
            # if product_price == "":
            #     return jsonify({"message":"Product price field cant be empty"}), 400
            # if product_price == " ":
            #     return jsonify({"message":"Product price field cant be passed empty string"}), 400
            # if not isinstance(product_name, str):
            #     return jsonify({"message":"Product name field can not be an int"}), 400    
            # if not isinstance(product_price, int):
            #     return jsonify({"message":"Product price field can not be a string"}), 400
            #  if new_product == "product exits ":
            #     return jsonify({'message': "product was not added"}), 401
            # return jsonify({'message': new_prooduct }), 201
            
            db.insert_new_product(product_name, product_price)
            return jsonify({'message': new_product.__dict__ }), 201

       
        except:
            return jsonify({"message":"Invalid input"}), 400


    @app.route("/api/v1/products/", methods=["GET"], strict_slashes=False)
    def get_all_prducts():
        products = db.get_all_products()
        return jsonify({"products":products})

    @app.route("/api/v1/products/", methods=["PUT"], strict_slashes=False)
    def modify_product():
        pass

    @app.route("/api/v1/products/", methods=["DELETE"], strict_slashes=False)
    def delete_product():
        pass
        
        
    @app.route("/api/v1/products/<int:product_id>", methods=["GET"], strict_slashes=False)
    def get_single_product(product_id):
        single_product = db.get_one_product(product_id)
        return jsonify({"single_product":single_product})



    @app.route("/api/v1/sales/", methods=["POST"], strict_slashes=False)
    def post_a_sale():
        """for posting a sale, id auto increments"""
    
        data = request.get_json()
        sale_quantity = data.get('sale_quantity')
        sale_price = data.get('sale_price')
        new_sale = Sale(sale_quantity, sale_price)


        # if sales_quantity == "":
        #     return jsonify({"message":"Sale qunatity field can not have space"}), 400
        # if sales_quantity == " ":
        #     return jsonify({"message":"Sale field can not be passed empty string"}), 400
        # if sales_price == "":
        #     return jsonify({"message":"Sales price field cant be empty"}), 400
        # if sales_price == " ":
        #     return jsonify({"message":"Sales price field cant be passed an empty string"}), 400
        # if not isinstance(sales_price, int):
        #     return jsonify({"message":"sale price field can not be a string"}), 400
        # if not isinstance(sales_quantity, str):
        #     return jsonify({"message":"sale quantity field should be an string"}), 400
        # for salesList in salesLists:
        #         if sales_quantity in salesList.sales_quantity:
        #             return jsonify({"response": "you have already registered this sale"}), 400
                    

        db.insert_new_sale(sale_quantity,sale_price)
        return jsonify({'message': new_sale.__dict__ }), 201
        

    @app.route("/api/v1/sales/", methods=["GET"], strict_slashes=False)
    def get_all_sales():
        sales = db.get_all_sales()
        return jsonify({"sales":sales})

    @app.route("/api/v1/sales/<int:sale_id>", methods=['GET'], strict_slashes=False)
    def get_single_sale(sale_id):
        single_sale = db.get_one_sale(sale_id)
        return jsonify({"single_sale":single_sale})

    return app