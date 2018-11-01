import unittest
import json
from API.controllers.controllers import start_app
from API.models.storedb import Database 


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = start_app()
        self.client = self.app.test_client()
        self.db = Database

    def test_login_passing(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client.post('/api/auth/login/',
                                    content_type="application/json",
                                    json=dict(user_name="follow", password="were"))
        respond = json.loads(result.data)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    
    def test_signup_passing(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client.post('/api/auth/signup',
                                    content_type="application/json",
                                    json=dict(user_name="jonathan", email="masete@gmail.com",
                                                         password=12345678))
        respond = json.loads(result.data)
        self.assertIn('user', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["user"])

    def test_signup_fail(self):
        """
            test for failling signup when a user leaves spaces in an email and declares password as string
        """
        result = self.client.post('/api/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="mwesigwa", email="bill @gmail.com",
                                                         password="dhccf")))        
        
        respond = json.loads(result.data.decode())
        self.assertEqual(result.status_code, 400)      
        self.assertTrue(respond["error"])
    
    def test_post_a_product_passing(self):
        """
            testing pssing product
        """
        result = self.client.post('/api/v1/products/',
                                    content_type="application/json",
                                    data=json.dumps(dict(product_name="LG",
                                                         product_price=12345678)))
        response = json.loads(result.data)
        self.assertIn("LG", response['message'])
        self.assertIn('message', response)
        self.assertIsInstance(response, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["message"])

    def test_get_one_product_route(self):
        """
        get one product route    
        """
        response = self.client.post('/api/v1/products/',content_type ="application/json",
                                       json=dict(product_name="LG",
                                        product_price=12345678))
        print(response)
        result = self.client.get('/api/v1/products/1')
        result2 = self.client.get('/api/v1/products/q')
        respond = json.loads(result.data)
        # self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)

    # def test_post_a_sale_passing(self):
    #     """
    #         tests for posting a sale
    #     """
    #     result = self.client.post('/api/v1/sales/',
    #                                 content_type="application/json",
    #                                 data=json.dumps(dict(sale_quantity=45,
    #                                         sale_price=12345678)))
    #     respond = json.loads(result.data.decode())
    #     self.assertEqual(12345678, respond['message']['sale_price'])
    #     self.assertIsInstance(respond, dict)
    #     self.assertEqual(result.status_code, 201)
    #     self.assertTrue(result.json["message"])

    def test_delete_product_pass(self):
        """
            testing for deleting a product
        """
        result = self.client.delete('/api/v1/products/1')
        response = json.loads(result.data)
        self.assertIn('There is no such product with that Id', response['response'])
        self.assertIsInstance(response, dict)
        self.assertEqual(result.status_code, 404)
    
    def test_modify_product(self):
        """
        tests for modifying a product  
        """
        result = self.client.put('/api/v1/products/6',
                                    content_type="application/json",
                                    json=dict(product_name="LG",
                                                         product_price=12345678))
        respond = json.loads(result.data)
        self.assertIn('product modified successfully', respond['message'])
        self.assertIsInstance(respond, dict)

    def test_single_sale_passing(self):
        """
        get one sale route    
        """
        result = self.client.get('/api/v1/sales/1',content_type="application/json")
        respond = json.loads(result.data)
        # self.assertIn("LG", respond)
        self.assertEqual(result.status_code, 200)
        # self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)

    def test_single_sale_passing_failing(self):
        """
        get one sale route    
        """
        result = self.client.get('/api/v1/sales/1',content_type="application/json")
        respond = json.loads(result.data)
        # self.assertIn("LG", respond)
        self.assertEqual(result.status_code, 200)
        # self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)
    


    if __name__ == '__main__':
        unittest.main()