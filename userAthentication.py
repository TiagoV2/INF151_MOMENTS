import os
import sqlite3

DATABASE_PATH = os.path.join(os.getcwd(), 'userData', 'user_credentials.db')



#all exisiting users will go here
def verifyUser(userName, password):
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM users WHERE userName = ? AND password = ?', (userName, password))
	user_data = cursor.fetchone()
	
	conn.close()
	
	return user_data is not None




#past usersi
def userNameIsUnique(userName):
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE userName = ?', (userName,))
	existing_user = cursor.fetchone()
	if existing_user:
		conn.close()
		return False
	return True
	

def createAccount(userName, password):
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()
	if not userNameIsUnique(userName):
		return False
	cursor.execute('INSERT INTO users (userName, password) VALUES (?, ?)', (userName, password))
	conn.commit()
	conn.close()
	printAllUsernames()
	return True

