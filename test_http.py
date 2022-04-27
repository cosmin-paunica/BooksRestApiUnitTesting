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
    
    def test_modify_book(self):
        with self.assertRaises(Exception) as cm:
            result = json.loads(self.app.put('/books/1').data)

    
test = MyTestCase()
test.setUp()
test.test_all_books()
test.test_all_authors()
test.test_modify_book()