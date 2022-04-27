from calendar import c
import sqlite3
from flask import Blueprint, request
from db_conn import get_db_connection

books = Blueprint('books', __name__)

@books.route('/books', methods=['GET'])
def get_all_books():
    conn = get_db_connection()
    book_rows = conn.execute('SELECT id, title, genre, publish_date FROM books')
    result = []
    for row in book_rows:
        result.append(dict(row))
    conn.close()
    return {"message": "success", "data": result}

@books.route('/books', methods=['POST'])
def add_book():
    conn = get_db_connection()
    data = request.get_json(force=True)

    try:
        title = data['title']
        publish_date = data['publish_date']
        genre = data['genre']
    except:
        conn.close()
        return {"message": "invalid data"}
    
    conn.execute("INSERT INTO books (title, publish_date, genre) VALUES (?, ?, ?)", (title, publish_date, genre))
    conn.commit()
    conn.close()

    return {"message": "successfully inserted new book"}

@books.route('/books/<title>', methods=['GET'])
def get_books_by_name(title):
    conn = get_db_connection()
    book_rows = conn.execute('SELECT id, title, publish_date,price, black_friday_price genre FROM books WHERE title = (?)', (title)).fetchall()

    result = []

    for row in book_rows:
        result.append(dict(row))
    
    conn.close()
    return {"message": "successfully retrieved all books by title " + title, "data": result}

@books.route('/books/<id>', methods=['PUT'])
def modify_book(id):
    conn = get_db_connection()
    data = request.get_json(force=True)
    if 'new_title' not in data or 'new_genre' not in data or 'new_publish_date' not in data or 'price' not in data or 'black_friday_price' not in data:
        raise('invalid data')
    try:
        new_title = data['new_title']
        new_genre = data['new_genre']
        new_publish_date = data['new_publish_date']
        new_price = data['new_price']
        new_black_friday_price = int(new_price) * 0.6
    except:
        conn.close()
        return {"message":"invalid data"}
    
    conn.execute('UPDATE books SET title = ?, genre = ?, publish_date = ?, price = ?, black_friday_price = ? WHERE id = ?', (new_title, new_genre, new_publish_date, new_price, new_black_friday_price, id))
    conn.commit()
    conn.close()
    return {"message": "successfully updated book with id " + id}

@books.route('/books<id>', methods=['DELETE'])
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    return {"message": "successfully deleted book with id " + id}

@books.route('/books/bf/<id>', methods=['GET'])
def get_prices(id):
    conn = get_db_connection()
    rows = conn.execute('SELECT price, black_friday_price FROM books WHERE id = ?', (id,))
    result = []
    for row in rows:
        result.append(dict(row))
    conn.close()
    return {"message":"success", "data": result}