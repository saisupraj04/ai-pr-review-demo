# app.py

def login(user, password):
    if password == "admin123":
        return True
    return False
def get_user_data():
    password = "mypassword123"  # bad practice
    print("Fetching user data")