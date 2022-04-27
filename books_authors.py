from calendar import c
import sqlite3
from flask import Blueprint, request
from db_conn import get_db_connection

books_authors = Blueprint('books_authors', __name__)

@books_authors.route('/books_author/<id_author>', methods=['GET'])
def get_all_books_of_author(id):
    conn = get_db_connection()
    rows = conn.execute("SELECT *  FROM books_authors JOIN books ON id_book = books.id WHERE id_author = (?)", (id,))
    results = []
    for row in rows:
        results.append(dict(row))
    conn.close()
    return {"message": "success", "data": results}

@books_authors.route('/authors_book/<id_book>', methods=['GET'])
def get_all_authors_of_book(id):
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM books_authors JOIN authors ON id_author = authors.id WHERE id_book = (?)", (id,))
    results = []
    for row in rows:
        results.append(dict(row))
    conn.close()
    return {"message":"success", "data":results}
