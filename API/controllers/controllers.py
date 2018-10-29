"""my controllers holding the HTTP requests"""
from flask import Flask, jsonify, request
from API.models.storedb import Database

def start_app():
    """starting  the flask instance"""
    app = Flask(__name__)


    @app.route("/", strict_slashes=False)
    def index():
        return jsonify({"message":"No products are available yet."})
        
    @app.route("/api/v1/products/", methods=["POST"], strict_slashes=False)
    def post_a_product():
        """params: none, post a product by postman"""
        try:
            feedback = request.get_json()
            product_name = feedback['product_name']
            product_price = feedback['product_price']

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

            new_product = Product(product_name, product_price)
            new_product.insert_new_product()

            if new_product == "product exits ":
                return jsonify({'message': "product was not added"}), 401
            return jsonify({'message': new_prooduct}), 201

        except:
            return jsonify({"message":"Invalid input"}), 400


    @app.route("/api/v1/products/", methods=["GET"], strict_slashes=False)
    def get_all_prducts():
        getback = []
        for pdtsList in pdtsLists:
            getback.append(pdtsList.myproducts())
        return jsonify(getback)

    @app.route("/api/v1/products/<int:product_id>", methods=["GET"], strict_slashes=False)
    def get_single_product(product_id):
        """params: product id
           for getting a product by id
        """
        single = []
        for pdtsList in pdtsLists:
            if pdtsList.product_id == product_id:
                req_dict = (pdtsList.myproducts())
                single.append(req_dict)
            if not single:
                return jsonify({"Products": "product does not exist"})
        else:
            return jsonify(single), 200

    salesLists = []


    @app.route("/api/v1/sales/", methods=["POST"], strict_slashes=False)
    def post_a_sale():
        """for posting a sale, id auto increments"""
        try:
            dad = request.get_json()
            sales_id = len(salesLists) + 1
            sales_quantity = dad['sales_quantity']
            sales_price = dad['sales_price']


            if sales_quantity == "":
                return jsonify({"message":"Sale qunatity field can not have space"}), 400
            if sales_quantity == " ":
                return jsonify({"message":"Sale field can not be passed empty string"}), 400
            if sales_price == "":
                return jsonify({"message":"Sales price field cant be empty"}), 400
            if sales_price == " ":
                return jsonify({"message":"Sales price field cant be passed an empty string"}), 400
            if not isinstance(sales_price, int):
                return jsonify({"message":"sale price field can not be a string"}), 400
            if not isinstance(sales_quantity, str):
                return jsonify({"message":"sale quantity field should be an string"}), 400
            for salesList in salesLists:
                    if sales_quantity in salesList.sales_quantity:
                        return jsonify({"response": "you have already registered this sale"}), 400
                        

            salesLists.append(AllSales(sales_id, sales_quantity, sales_price))
            return jsonify({"message": "a sale now exists"}), 201
        except:
            return jsonify({"message":"Invalid input"}), 400

    @app.route("/api/v1/sales/", methods=["GET"], strict_slashes=False)
    def get_all_sales():
        """get all sales"""
        getin = []
        for salesList in salesLists:
            getin.append(salesList.mysales())
        return jsonify(getin)

    @app.route("/api/v1/sales/<int:sales_id>", methods=['GET'], strict_slashes=False)
    def get_single_sale(sales_id):
        """params: None
           routes for getting a single sale
        """
        response = []
        for saleList in salesLists:
            if saleList.sales_id == sales_id:
                req_dict = (saleList.mysales())
                response.append(req_dict)
        if not response:
            return jsonify({'Sales': 'sales not found'}), 200
        else:
            return jsonify(response), 200

    return app