import sqlite3

def connect():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INT, genre TEXT) ")
    conn.commit()
    conn.close()

def insert(title, author, year, genre):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, genre))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" SELECT * FROM book ")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", genre=""):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" SELECT * FROM book WHERE title=? OR author=? OR year=? OR genre=? ", (title, author, year, genre))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" DELETE FROM book WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, genre):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute(" UPDATE book SET title=?, author=?, year=?, genre=? WHERE id=?", (title, author, year, genre, id))
    conn.commit()
    conn.close()

connect()
