from flask import Flask
from authors import authors
from books import books
from books_authors import books_authors

app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(authors)
app.register_blueprint(books_authors)
