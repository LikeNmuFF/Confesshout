import sqlite3


# Database creation:

conn = sqlite3.connect('db/confeshout.db')
cursor = conn.cursor()

# Database table creation:

cursor.execute('''
	CREATE TABLE IF NOT EXISTS submission(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		message TEXT NOT NULL,
		username TEXT,
		course TEXT,
		year_level TEXT,
		status TEXT DEFAULT 'pending',
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		)

	''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
			id INtEGER PRIMARY KEY AUTOINCREMENT,
			username TEXT,
			password TEXT,
			role TEXT DEFAULT 'user'
			)
               
               ''')

conn.commit()
conn.close()
print("success")