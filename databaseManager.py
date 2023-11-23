import sqlite
import os

DATABASE_PATH = os.path.join(os.getcwd(), 'userData', 'user_credentials.db')

def removeUser(userName):
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE userName = ?', (userName,))
	existingUser = cursor.fetchone()
	if existingUser:
		cursor.execute('DELETE FROM users WHERE userName = ?', (userName,))
		conn.commit()
		conn.close()
		return True
	else:
		conn.close()
		return False

def changePassword(userName):
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE userName = ?', (userName,))
	existingUser = cursor.fetchone()
	if existingUser:
		cursor.execute('UPDATE users SET password = ? WHERE userName = ?', (new_password, userName))
		conn.commit()
		conn.close()
		return True
	else:
		conn.close()
		return False
	

def printAllUsernames():
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute('SELECT userName FROM users')
	usernames = cursor.fetchall()

	conn.close()

	for username in usernames:
		print("Username:", username[0])

