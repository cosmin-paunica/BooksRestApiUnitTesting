import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

books_to_insert = [
    ('1984', 'Dystopian', '1949-06-08'),
    ('Ion', 'Roman realist', '1920-11-20'),
    ('Animal Farm', 'Dystopian', '1945-08-17')
]

cur.executemany("INSERT INTO books(title, genre, publish_date) VALUES (?, ?, ?)", books_to_insert)

authors_to_insert = [
    ('George Orwell',),
    ('Liviu Rebreanu',)
]

cur.executemany("INSERT INTO authors (full_name) VALUES (?)", authors_to_insert)

cur.execute("INSERT INTO books_authors(id_book, id_author) VALUES (?, ?)", (1,1))
cur.execute("INSERT INTO books_authors(id_book, id_author) VALUES (?, ?)", (2,2))
cur.execute("INSERT INTO books_authors(id_book, id_author) VALUES (?, ?)", (3,1))

connection.commit()
connection.close()