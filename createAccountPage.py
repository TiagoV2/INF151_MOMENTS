# define and create the login page for an existing user

import tkinter as tk

def createAccountPage(root):
    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not password:
            info_label.config(text="Please fill in all fields.")
        elif password != confirm_password:
            info_label.config(text="Password and Confirm Password do not match.")
        else:
            info_label.config(text="Account created successfully!")

    create_account_frame = tk.Frame(root)
    create_account_frame.pack()

    username_label = tk.Label(create_account_frame, text="Username")
    username_label.pack()

    username_entry = tk.Entry(create_account_frame)
    username_entry.pack()

    password_label = tk.Label(create_account_frame, text="Password")
    password_label.pack()

    password_entry = tk.Entry(create_account_frame, show="*")
    password_entry.pack()

    confirm_password_label = tk.Label(create_account_frame, text="Confirm Password")
    confirm_password_label.pack()

    confirm_password_entry = tk.Entry(create_account_frame, show="*")
    confirm_password_entry.pack()

    create_account_button = tk.Button(create_account_frame, text="Create Account", command=create_account)
    create_account_button.pack()

    info_label = tk.Label(create_account_frame, text="")
    info_label.pack()

