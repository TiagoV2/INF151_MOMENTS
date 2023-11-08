import firebase_admin
from firebase_admin import credentials,auth
import userRepository

cred = credentials.Certificate("auth/moments-404519-firebase-adminsdk-zknme-dc5669db02.json")
firebase_admin.initialize_app(cred)

def register_user(email, password, name, username,dob=""):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"Successfully registered user with UID: {user.uid}")
        m_user = userRepository.userRepo(user.uid,email,name,username,dob)
        print("created m_user", m_user.get_name())
        return (user,m_user)
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        print(f"User {email} is logged in with UID: {user.uid}")
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def log_out(uid):
    try:
        # Revoke the user's refresh tokens, which will log them out
        auth.revoke_refresh_tokens(uid)
        print(f"Successfully logged out user with UID: {uid}")
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == '__main__':
    testing = False
    if testing:
        dummy_email = 'testFunc1@test.com'
        dummy_password = '12345678'
        dummy_name = 'test'
        dummy_username = 'tester'
        u1 = register_user(dummy_email, dummy_password,dummy_name,dummy_username)
        m1 = u1[1]
        login_user(m1.get_email(), '12345678')
        log_out(m1.get_uid())