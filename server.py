from bottle import Bottle, request, redirect, template, run, response
from pymongo import MongoClient

"""
Author: Muhammad Mahad Mirza

This code establishes a connection to a MongoDB cluster using the MongoClient class from the PyMongo library. It 
connects to a MongoDB database named 'userreview' and collection named 'login'. The connection string includes the 
username, password, and cluster information required for authentication and connection.

"""
cluster = MongoClient("mongodb+srv://mahadmirza545:Mahad1234@cluster0.yqjy6mb.mongodb.net/?retryWrites=true&w=majority")
db = cluster["userreview"]
users_collection = db["login"]
reviews_collection = db["reviews"]
# Create a Bottle web application
app = Bottle()


# Serve static files (CSS)
@app.route('/')
def home():
    return template('homepage')


@app.route('/login')
def login():
    return template('login.tpl')


"""
Author: Muhammad Mahad Mirza
Route for handling user login.
This route handles HTTP POST requests to the '/login' endpoint. It extracts the 'username' and 'password' parameters 
from the form data submitted by the user. It then queries a 'users_collection' to find a user with the provided 
'username'. If a user is found and their 'password' matches the provided password, it sets a cookie with the user's 
'username' and redirects the user to the 'dashboard.tpl' template. If the user is not found or the password does not 
match, it returns an error message indicating 'Invalid username or password'.

HTTP Method: POST

Route URL: /login

Parameters:
    - 'username' (str): The username provided by the user.
    - 'password' (str): The password provided by the user.

Returns:
    - If a valid user is found and the password matches, it sets a cookie and redirects to the dashboard.
    - If the user is not found or the password is incorrect, it returns an error message as a string.

Example Usage:
    POST /login
    Request Data: {'username': 'john_doe', 'password': 'secretpassword'}
    - If 'john_doe' with the correct password exists, it sets a cookie and redirects to the dashboard.
    - If the username doesn't exist or the password is incorrect, it returns 'Invalid username or password'.
"""
@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = users_collection.find_one({"username": username})

    if user and user["password"] == password:
        response.set_cookie('username', username)
        return template('dashboard.tpl')
    else:
        return "Invalid username or password"


@app.route('/profile')
def profile():
    return template('profile')


# Define a route for the sign-up page
@app.route('/signup')
def signup():
    return template('signup.tpl')



python
Copy code
"""
Author: Muhammad Mahad Mirza

Route for user registration (sign-up).

This route handles HTTP POST requests to the '/signup' endpoint, allowing users to create new accounts. 
It expects the following parameters in the form data:
    - 'first_name' (str): The user's first name.
    - 'last_name' (str): The user's last name.
    - 'username' (str): The desired username for the new account.
    - 'email' (str): The user's email address.
    - 'password' (str): The password for the new account.

Before creating a new account, it checks if the provided 'username' already exists in the 'users_collection'. 
If the 'username' is found, it returns an error message indicating that the username is already taken. If the 
'username' is unique, it generates a new 'user_id' by counting the existing user documents and incrementing 
the count by one.

A new user document is created with the provided information, including a unique 'user_id'. 
The password is stored as-is in this example, but it is recommended to hash the password for security 
in a real application.

The new user document is then inserted into the 'users_collection'. For this example, it returns a success message 
to indicate that the sign-up was successful, including the user's name and username.

HTTP Method: POST

Route URL: /signup

Parameters:
    - 'first_name' (str): The user's first name.
    - 'last_name' (str): The user's last name.
    - 'username' (str): The desired username for the new account.
    - 'email' (str): The user's email address.
    - 'password' (str): The password for the new account.

Returns:
    - If the 'username' is unique, it creates a new user, inserts it into the 'users_collection', 
    and returns a success message.
    - If the 'username' is already taken, it returns an error message indicating that the username is not available.

Example Usage:
    POST /signup
    Request Data: {'first_name': 'John', 'last_name': 'Doe', 'username': 'john_doe', 'email': 'john.doe@example.com',
     'password': 'secretpassword'}
    - If 'john_doe' is not already in use, it creates a new user and returns a success message.
    - If 'john_doe' is already taken, it returns 'Username already exists. Please choose a different username.'
"""
@app.route('/signup', method='POST')
def do_signup():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    username = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')

    # Check if the username already exists
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return "Username already exists. Please choose a different username."

    # Count the number of existing users to generate a unique ID
    user_count = users_collection.count_documents({})
    user_id = user_count + 1

    # Create a new user document
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password  # Note: In a real application, hash the password for security
    }

    # Insert the new user into the 'users_collection'
    users_collection.insert_one(user)

    # For this example, you can return a success message
    return f"Sign-up successful for {first_name} {last_name} with username {username}"


@app.route('/reviews')
def reviews():
    return template('reviews')


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
