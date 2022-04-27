from calendar import c
import sqlite3
from flask import Blueprint, request
from db_conn import get_db_connection

authors = Blueprint('authors', __name__)

@authors.route('/authors', methods=['GET'])
def get_all_authors():
    conn = get_db_connection()
    author_rows = conn.execute('SELECT full_name FROM authors')
    result = []
    for row in author_rows:
        result.append(dict(row))
    conn.close()
    return {"message":"success", "data": result}

@authors.route('/authors', methods=['POST'])
def add_author():
    conn = get_db_connection()
    data = request.get_json(force=True)
    try:
        full_name = data['full_name']

    except:
        conn.close()
        return {"message":"invalid data"}
    
    conn.execute("INSERT INTO authors (full_name) VALUES (?)", (full_name,))
    conn.commit()
    conn.close()

    return {"message":"success"}

@authors.route('/authors/<full_name>', methods=['GET'])
def get_authors_by_full_name(full_name):
    conn = get_db_connection()
    author_rows = conn.execute("SELECT full_name FROM authors WHERE full_name = (?)", (full_name,))
    result = []
    for row in author_rows:
        result.append(dict(row))
    conn.close()
    return {"message":"success", "data":"result"}

@authors.route('/authors/<id>', methods=['PUT'])
def modify_author(id):
    conn = get_db_connection()
    data = request.get_json(force=True)
    try:
        new_full_name = data['full_name']
    except:
        conn.close()
        return {"message":"invalid data"}
    conn.execute("UPDATE authors SET full_name = ? WHERE id = ?", (new_full_name, id))
    conn.commit()
    conn.close()
    return {"message":"success"}

@authors.route('/authors/<id>', methods=['DELETE'])
def delete_author(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM authors WHERE id = ?', (id,))
    conn.commit()
    return {"message":"success"}