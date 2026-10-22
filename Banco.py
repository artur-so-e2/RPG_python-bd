import sqlite3 as sqlite

conn = sqlite.connect('rpg.bd')

conn.execute("DROP TABLE IF EXISTS classes")

conn.execute("CREATE TABLE classes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

conn.commit()
