import sqlite3
conn = sqlite3.connect("db/database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
conn.close()