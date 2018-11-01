"""my controllers holding the HTTP requests"""
from flask import Flask, jsonify, request
from cerberus import Validator
from API.models.storedb import Database
from API.models.models import Product, Sale
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from API.validation_schema import signup_schema, login_schema,post_product_schema,post_sale_schema,modify_product_schema,delete_product_schema,get_sale_schema


db = Database()

val = Validator()

def start_app():
    """starting  the flask instance"""
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']='masete'
    jwt= JWTManager(app)


    @app.route("/", strict_slashes=False)
    def index():
        return jsonify({"message":"No products are available yet."})
        
    
    @app.route("/api/auth/signup/", methods=["POST"], strict_slashes=False)
    @jwt_required
    def signup():

        data = request.get_json()
        user_name = data.get('user_name')
        email = data.get('email')
        password = data.get('password')
        print(data)

        validate = val.validate(data, signup_schema)
        print(val.errors)
        if not validate:
            return jsonify({'error': val.errors}), 400

        add_user =db.signup(user_name,email,password)
        return jsonify({"user":add_user}), 201


    @app.route("/api/auth/login/", methods=["POST"], strict_slashes=False)
    def login():  
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        data = request.get_json()
        user_name = data.get('user_name')
        password  = data.get('password')

        validate = val.validate(data, login_schema)
        if not validate:
            return jsonify({'error': val.errors}), 400


        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=user_name)
        return jsonify(access_token=access_token), 200

    
    @app.route("/api/v1/products/", methods=["POST"], strict_slashes=False)
    @jwt_required
    def post_a_product():
        """params: none, post a product by postman"""
        
    
        data = request.get_json()
        product_name = data['product_name']
        product_price = data['product_price']
        # new_product = Product(product_id=None, product_name, product_price)

        validate = val.validate(data, post_product_schema)
        if not validate:
            return jsonify({'error': val.errors}), 400

        db.insert_new_product(product_name, product_price)
        return jsonify({'message': "{} has been added".format(product_name)}), 201




    @app.route("/api/v1/products/", methods=["GET"], strict_slashes=False)
    @jwt_required
    def get_all_prducts():
        products = db.get_all_products()
        return jsonify({"products":products})

    @app.route("/api/v1/products/<int:products_id>", methods=["PUT"], strict_slashes=False)
    @jwt_required
    def modify_product(products_id):
        data = request.get_json()
        product_name = data.get('product_name')
        product_price = data.get('product_price')

        validate = val.validate(data, modify_product_schema)
        if not validate:
            return jsonify({'error': val.errors}), 400

        modify = db.modify_product(products_id, product_name,product_price)
        product = db.get_one_product(products_id)
        
        return jsonify({"message":"product modified successfully",
                        "product":product}
                     )

    @app.route("/api/v1/products/<int:products_id>", methods=["DELETE"], strict_slashes=False)
    @jwt_required
    def delete_product(products_id):

        product = db.get_product_by_id(products_id)
        if not product:
            return jsonify({"response": "There is no such product with that Id"}), 404
        db.delete_product(products_id)
        return jsonify({"message": "Product has been deleted successfully"})

        
        
    @app.route("/api/v1/products/<int:product_id>", methods=["GET"], strict_slashes=False)
    @jwt_required
    def get_single_product(product_id):
        single_product = db.get_one_product(product_id)
        if not single_product:
            return jsonify({"error":"product does not exist"}),404
        return jsonify({"single_product":single_product}),200



    @app.route("/api/v1/sales/", methods=["POST"], strict_slashes=False)
    @jwt_required
    def post_a_sale():
        """for posting a sale, id auto increments"""
    
        data = request.get_json()
        sale_quantity = data.get('sale_quantity')
        sale_price = data.get('sale_price')
        new_sale = Sale(sale_quantity, sale_price)

        validate = val.validate(data, post_sale_schema)
        if not validate:
            return jsonify({'error': val.errors}), 400

        db.insert_new_sale(sale_quantity,sale_price)
        return jsonify({'message': new_sale.__dict__ }), 201
        

    @app.route("/api/v1/sales/", methods=["GET"], strict_slashes=False)
    @jwt_required
    def get_all_sales():
        sales = db.get_all_sales()
        return jsonify({"sales": sales}), 200

    @app.route("/api/v1/sales/<int:sale_id>", methods=['GET'], strict_slashes=False)
    @jwt_required
    def get_single_sale(sale_id):
        single_sale = db.get_one_sale(sale_id)
        if not single_sale:
            return jsonify({"error":"sale does not exist"}),404
        return jsonify({"single_sale":single_sale})


    return app