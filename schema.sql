DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books_authors;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    publish_date DATE NOT NULL
);

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL
);

CREATE TABLE books_authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_book INTEGER,
    id_author INTEGER,
    FOREIGN KEY(id_book) REFERENCES books(id),
    FOREIGN KEY(id_author) REFERENCES authors(id)
);
