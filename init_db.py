import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Database creation:
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Database table creation:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS submission(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL,
        username TEXT,
        course TEXT,
        year_level TEXT,
        status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'approved', 'rejected')),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    )
''')


conn.commit()
conn.close()
print("success")

