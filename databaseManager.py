import sqlite3
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
	
def getCurrentUserName():
    # This function retrieves the current user's name from the database
    # You may need to pass some identifier for the current user (e.g., user ID) to this function
    # and modify the SQL query accordingly
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT userName FROM users WHERE user_id = ?', (current_user_id,))
    current_user_name = cursor.fetchone()[0]  # Fetch the first column of the result (username)
    conn.close()
    return current_user_name

def printAllUserNames():
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute('SELECT userName FROM users')
	usernames = cursor.fetchall()

	conn.close()

	for username in usernames:
		print("Username:", username[0])

if __name__ == "__main__":
	printAllUserNames()
