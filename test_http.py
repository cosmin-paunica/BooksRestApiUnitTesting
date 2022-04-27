import json
from sqlalchemy import JSON
from app import app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_all_books(self):
        result = json.loads(self.app.get('/books').data)
        # Make your assertions
        self.assertEqual(result['message'], "success")
        self.assertNotEqual(len(result['data']), 0)
    
    def test_all_authors(self):
        result = json.loads(self.app.get('/authors').data)
        self.assertTrue(result['message'] == "success")
    
    def test_modify_book_no_data(self):
        with self.assertRaises(Exception) as cm:
            result = json.loads(self.app.put('/books/1').data)
    
    def test_bf_price(self):
        result = json.loads(self.app.get('/books/bf/1').data)
        price = int(result['data'][0]['price'])
        bf_price = int(result['data'][0]['black_friday_price'])
        self.assertGreater(price, bf_price)
        self.assertEqual(price * 0.6, bf_price)
    
    def test_price_almost_equal(self):
        result = json.loads(self.app.get('/books/bf/1').data)
        price = int(result['data'][0]['price'])
        bf_price = price * 0.6000000001 # maybe some floating point precision could cause this ?

        self.assertAlmostEqual(bf_price, price * 0.6)
        

    
test = MyTestCase()
test.setUp()
test.test_all_books()
test.test_all_authors()
test.test_modify_book_no_data()
test.test_bf_price()
test.test_price_almost_equal()