from flask import Flask
from app import app
import unittest
import json


class FunctionalTesting(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_case_1(self):
        id = 1
        result = self.app.put(f'/books/{id}', data=json.dumps({
            "black_friday_price": 4,
            "genre": "Dystopian",
            "price": 7,
            "publish_date": "1949-06-08",
            "title": "1984"
        }))
        self.assertEqual(json.loads(result.data)['message'], f"successfully updated book with id {id}")
    
    def test_case_2(self):
        id = 1
        result = self.app.delete(f'/books/{id}')
        self.assertEqual(json.loads(result.data)['message'], f"successfully deleted book with id {id}")

    def test_case_3(self):
        with self.assertRaises(Exception) as cm:
            result = json.loads(self.app.put('/books/2').data)
    
    def test_case_4(self):
        id = 7
        result = self.app.delete(f'/books/{id}')
        self.assertEqual(json.loads(result.data)['message'], f"book with id {id} does not exist")
        self.assertEqual(1, 2)


import init_db