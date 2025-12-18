# Simple Login Module

def login(username, password):
    correct_username = "admin"
    correct_password = "admin123"

    if username == correct_username and password == correct_password:
        print("Login successful")
    else:
        print("Invalid username or password")


# Test the login function
user = input("Enter username: ")
pwd = input("Enter password: ")

login(user, pwd)
