import sqlite3
import json

Connection = sqlite3.connect("books.db")
cursor = Connection.cursor()

with open("books.json","r")as f:
    data = json.load(f)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    rating INTEGER,
    availability TEXT)
''')
for book in data:
    cursor.execute('''
        INSERT INTO books (title ,price ,rating ,availability) VALUES (? ,? ,? ,?)
    ''',( 
    book["title"],
    book["price"],
    book["rating"],
    book["availability"]
    ))

Connection.commit()

print(f"Inserted {len(data)} books into books.db")
