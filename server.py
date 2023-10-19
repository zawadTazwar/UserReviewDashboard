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
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')

        user = users_collection.find_one({"_id": username})
        if user:
            return "Username already exists"
        else:
            users_collection.insert_one({"_id": username, "password": password})
            return "You were successfully registered"

    return template('signup.tpl')


@app.route('/reviews')
def reviews():
    return template('reviews')


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
