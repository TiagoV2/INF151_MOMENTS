import sqlite3

conn = sqlite3.connect('user_credentials.db')
cursor = conn.cursor()

create_table_sql = '''
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
'''
cursor.execute(create_table_sql)
conn.commit()
conn.close()

