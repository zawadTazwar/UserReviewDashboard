from bottle import Bottle, request, redirect, template, run, response
from pymongo import MongoClient

"""
Author: Muhammad Mahad Mirza

This code establishes a connection to a MongoDB cluster using the MongoClient class from the PyMongo library. It 
connects to a MongoDB database named 'userreview' and a collection named 'login'. The connection string includes the 
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


# Route for handling login form submissions



@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = users_collection.find_one({"_id": username})

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


# Define a route to handle form submissions



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
