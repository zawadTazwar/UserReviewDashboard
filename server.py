from bottle import Bottle, request, redirect, template, run, response
from pymongo import MongoClient
from bson import ObjectId


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

"""
Author: Muhammad Mahad Mirza

Route for user registration (sign-up).

This route handles HTTP POST requests to the '/signup' endpoint, allowing users to create new accounts. It expects the 
following parameters in the form data:
    - 'first_name' (str): The user's first name.
    - 'last_name' (str): The user's last name.
    - 'username' (str): The desired username for the new account.
    - 'email' (str): The user's email address.
    - 'password' (str): The password for the new account.

Before creating a new account, it checks if the provided 'username' already exists in the 'users_collection'. 
If the 'username' is found, it returns an error message indicating that the username is already taken. If the 'username'
 is unique, it generates a new 'user_id' by counting the existing user documents and incrementing the count by one.

A new user document is created with the provided information, including a unique 'user_id'. The password is stored as-
is in this example, but it is recommended to hash the password for security in a real application.

The new user document is then inserted into the 'users_collection'. For this example, it returns a success message to 
indicate that the sign-up was successful, including the user's name and username.

HTTP Method: POST

Route URL: /signup

Parameters:
    - 'first_name' (str): The user's first name.
    - 'last_name' (str): The user's last name.
    - 'username' (str): The desired username for the new account.
    - 'email' (str): The user's email address.
    - 'password' (str): The password for the new account.

Returns:
    - If the 'username' is unique, it creates a new user, inserts it into the 'users_collection', and returns a success 
    message.
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

"""
Author: Md Jawad Ul Tazwar

Routes:
-------
/dashboard:
    Displays the user's dashboard containing all their reviews. If the user is not logged in, they are redirected 
    to the login page.

/edit_review/<review_id>:
    Displays the edit page for a particular review specified by its unique ID. If the review with the provided ID 
    is not found, a message is displayed to the user.

/update_review:
    Updates a review in the database with the edited content from the user. After updating, the user is redirected 
    back to the dashboard.

/delete_review/<review_id>:
    Deletes a review specified by its unique ID from the database. After deletion, the user is redirected back 
    to the dashboard.

/create_review:
    Displays the page for creating a new review.

/store_review:
    Stores the newly created review in the database. The review is associated with the logged-in user. After storage,
    the user is redirected back to the dashboard.

Dependencies:
-------------
* reviews_collection: This represents the MongoDB collection that contains all the reviews. Operations such as 
  finding, updating, and deleting reviews are performed on this collection.

* ObjectId: It's a utility from the MongoDB library to handle the unique object IDs associated with each document.


"""


@app.route('/dashboard')
def dashboard():
    username = request.get_cookie('username')
    if not username:
        # If the user is not logged in, redirect to login
        redirect("/login")

    # Fetch user reviews from the database
    user_reviews = list(reviews_collection.find({"username": username}))

    return template('dashboard.tpl', reviews=user_reviews)

# Route for editing a review
@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})

    if not review:
        return "Review not found"

    return template('edit_review.tpl', review=review)

# Route for updating a review after editing
@app.route('/update_review', method='POST')
def update_review():
    review_id = request.forms.get('review_id')
    content = request.forms.get('content')

    reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$set": {"content": content}})

    redirect('/dashboard')

# Route for deleting a review
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    reviews_collection.delete_one({"_id": ObjectId(review_id)})

    redirect('/dashboard')



# Route for creating a new review
@app.route('/create_review')
def create_review():
    return template('create_review.tpl')


@app.route('/store_review', method='POST')
def store_review():
    title = request.forms.get('title')
    content = request.forms.get('content')
    username = request.get_cookie('username')


    review = {
        "username": username,
        "title": title,
        "content": content
    }

    reviews_collection.insert_one(review)

    redirect('/dashboard')

if __name__ == '__main__':
    run(app, host='localhost', port=8080)