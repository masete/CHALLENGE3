# CHALLENGE3
continuation of challenge 2 of shop manager

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Features
    Admin can login
    Attendant can login
-   Admin can add a product
-   Admin or store attendant can get all products
-   Admin or store attendant can get a specific product.
-   Store attendant can add a sale order.
-   Admin can get all sale order details.

## API Endpoints

| REQUEST | ROUTE                           | FUNCTIONALITY                 |
| ------- | ------------------------------- | ----------------------------- |
| POST    | /api/auth/login                 | Admin or attendant logs in    |
| POST    | /api/auth/signup                | Admin signs up attendant      |
| GET     | /api/v1/products                | Fetches all products          |
| GET     | api/v1/products/&lt;product_id> | Fetches a single product      |
| GET     | api/v1/sales                    | Fetches all sales records     |
| GET     | api/v1/sales/&lt;sales_id>      | Fetches a single sales record |
| POST    | api/v1/products                 | Creates a product             |
| POST    | api/v1/sales                    | Creates a sales order         |
| PUT     | api/v1/products/&lt;product_id> | Modifies a product            |
| DELETE  | api/v1/products/&lt;product_id> | Deletes a product             |

### Getting started with the app

### Technologies used to build the application

-   [Python 3.6](https://docs.python.org/3/)
-   [Flask](http://flask.pocoo.org/)

### Installation

Create a new directory and initialize git in it. Clone this repository by running

```sh
git clone https://github.com/masete/CHALLENGE3/
```

Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using

```sh
virtualenv venv
```

Activate the virtual environment

```sh
cd venv/scripts/activate
```

Install the dependencies in the requirements.txt file using pip

```sh
pip install -r requirements.txt
```

Start the application by running

```sh
python run.py
```

Test your setup using [postman](www.getpostman.com) REST-client

### Running tests

-   Install nosetests
-   Navigate to project root
-   Use `nosetests tests/` to run the tests
-   To run tests with coverage, use `nosetests --with-coverage --cover-package=app && coverage report`

### Link to Store Manager on Heroku

### 

