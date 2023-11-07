import tkinter as tk
from createAccountPage import createAccountPage

def loginPage(root):
    login_frame = tk.Frame(root)
    login_frame.pack()

    email_label = tk.Label(login_frame, text="Email/Username")
    email_label.pack()

    email_entry = tk.Entry(login_frame)
    email_entry.pack()

    password_label = tk.Label(login_frame, text="Password")
    password_label.pack()

    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack()

    create_account_button = tk.Button(login_frame, text="Create Account", command=lambda: createAccountPage(root))
    create_account_button.pack()

