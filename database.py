import sqlite3


class Database:
	def __init__(self):
		self.conn = sqlite3.connect("batabase.db")
		self.cursor = self.conn.cursor()
		self.create()

	def add(self, title, author, description, genre):
		self.cursor.execute("INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)", (title, author, description, genre))
		self.conn.commit()

	def delete(self, id):
		self.cursor.execute("DELETE FROM books WHERE id = ?", (id,))
		self.conn.commit()

	def get(self):
		self.cursor.execute("SELECT * FROM books")
		return self.cursor.fetchall()

	def search(self, q):
		self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{q}%", f"%{q}%"))
		return self.cursor.fetchall()

	def create(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, description TEXT, genre TEXT)")
		self.conn.commit()
