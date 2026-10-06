import sqlite3


def insert_user(username, password, role):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO user (username, password, role) VALUES (?,?,?)
        ''',
        (username, password, role)
    )
    conn.commit()
    conn.close()


insert_user("admin", "CCSadminkid", "admin")
